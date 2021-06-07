import math

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules import conv

from models.models import BaseNetwork
from game.game import Action
import os
import json
import pickle

# from networks.spectral import eigen, laplacean
from configs.Configure import configuration as con
from configs.Configure import shapes

from numpy.random import seed

seed(1)

def conv3x3(in_channels, out_channels, stride=1, padding=1):
    return nn.Conv2d(
        in_channels, out_channels, kernel_size=3, stride=stride, padding=padding, bias=False
    )

def adaptiveAvgPool(shape):
    return nn.AdaptiveAvgPool2d(shape)

def adaptiveMaxPool(shape):
    return nn.AdaptiveMaxPool2d(shape)

def relu(x):
    return F.relu(x)

class DefaultNetwork(BaseNetwork):

    def __init__(self,
                 action_size: int = 0,
                 load_path: str = None):
        super().__init__(load_path=load_path)
        # regularizer = regularizers.l2(weight_decay)
        if con['continue_training']:
            load_path = con['load_path']
        
        # self.policy_network = None
        # self.value_network = None
        # self.reward_network = None 
        # self.representation_network = None
        self.meta_data = None
        if load_path:
            self.policy_network, self.value_network, self.reward_network, self.representation_network, self.meta_data = self.load_networks(load_path)
            self.action_size = self.meta_data['action_size']
        else:
            self.action_size = action_size
            
            input_features = shapes['output_size']
            
            self.value_network = nn.Sequential(
                nn.Linear(input_features, con['hidden_value']),
                nn.SELU(),
                nn.Linear(con['hidden_value'], 3)
            ).cuda()
            
            self.reward_network = nn.Sequential(
                nn.Linear(shapes['x_out_shape'], con['hidden_reward']),
                nn.SELU(),
                nn.Linear(con['hidden_reward'], 1)
            ).cuda()
            
            self.policy_network = nn.Sequential(
                nn.Linear(input_features, con['hidden_policy']),
                nn.SELU(),
                nn.Linear(con['hidden_policy'], action_size)
            ).cuda()
            
            self.representation_network = RepresentationNetwork().cuda()
            # value_network = torch.nn.Sequential([Dense(con['hidden_value'], activation='selu', kernel_regularizer=regularizer,
            #                                   kernel_initializer='lecun_normal', bias_initializer="lecun_normal",
            #                                   input_dim=shapes['output_size']),
            #                             Dense(3, kernel_regularizer=regularizer, input_dim=con['hidden_value'])])

            # reward_network = Sequential([Dense(con['hidden_reward'], activation='selu', kernel_regularizer=regularizer,
            #                                   kernel_initializer='lecun_normal', bias_initializer="lecun_normal",
            #                                    input_dim=(shapes['x_out_shape'])),
            #                             Dense(1, kernel_regularizer=regularizer, input_dim=con['hidden_reward'],
            #                                   activation=None)])

            # policy_network = Sequential([Dense(con['hidden_policy'], activation='selu', kernel_regularizer=regularizer,
            #                                    kernel_initializer='lecun_normal', bias_initializer="lecun_normal",
            #                                    input_dim=shapes['output_size']),
            #                              Dense(action_size, kernel_regularizer=regularizer,
            #                                    input_dim=con['hidden_policy'])])
        BaseNetwork.set_networks(self, self.value_network, self.reward_network, self.policy_network, self.representation_network)

    def load_networks(self, file_path='./saved-models'):
        self.policy_network = torch.load(os.path.join(file_path, 'policy_network.pth'))
        self.value_network = torch.load(os.path.join(file_path, 'value_network.pth'))
        self.reward_network = torch.load(os.path.join(file_path, 'reward_network.pth'))
        self.representation_network = torch.load(os.path.join(file_path, "representation_network.pth"))

        with open(os.path.join(file_path,'meta_data.json'),'r') as g:
            self.meta_data = json.load(g)

        print("loaded model")
        return self.policy_network, self.value_network, self.reward_network, self.representation_network, self.meta_data

    def save_networks(self,file_path='./saved-models'):
        torch.save(self.policy_network, os.path.join(file_path,'policy_network.pth'))
        torch.save(self.value_network, os.path.join(file_path,'value_network.pth'))
        torch.save(self.reward_network, os.path.join(file_path, 'reward_network.pth'))
        torch.save(self.representation_network, os.path.join(file_path, 'representation_network.pth'))

        meta_data = {'action_size': self.action_size,
                     'training_steps': self.training_steps}

        with open(os.path.join(file_path, 'meta_data.json'),'w') as g:
            json.dump(self.meta_data,g)
        print("Saved model")

    def _value_transform(self, value_support: np.array) -> float:
        """
        The value is obtained by first computing the expected value from the discrete support.
        Second, the inverse transform is then apply (the square function).
        """

        support = np.array([-1,0,1])
        value = self._softmax(value_support)
        value = np.dot(value, support)
        return value

    def _reward_transform(self, reward: np.array) -> float:
        """
        Stable sigmoid function in numpy
        """
        sigmoid =  np.piecewise(reward, [reward >= 0, reward<0], [lambda x: 1 / (1 + np.exp(-x)), lambda x: np.exp(x) / (1 + np.exp(x))])
        return sigmoid[0][0]
    
    def _conditioned_hidden_state(self, hidden_state, action: Action) -> np.array:
        conditioned_hidden = np.concatenate((hidden_state, np.eye(self.action_size)[action.index]))
        return np.expand_dims(conditioned_hidden, axis=0)

    def _softmax(self, values):
        """Compute softmax using numerical stability tricks."""
        values_exp = np.exp(values - np.max(values))
        return values_exp / np.sum(values_exp)


class RepresentationNetwork(nn.Module):
    def __init__(self):
        super(RepresentationNetwork, self).__init__()
        # for U
        self.conv1_1_U = conv3x3(12, 32)
        self.conv1_2_U = conv3x3(32, 64)
        self.max_pool_1_U = nn.MaxPool2d(2)
        
        self.conv2_1_U = conv3x3(64, 64)
        self.conv2_2_U = conv3x3(64, 128)
        
        self.max_pool_2_U = nn.MaxPool2d(2)
        
        self.conv3_1_U = conv3x3(128, 128)
        self.conv3_2_U = conv3x3(128, 256)
        
        self.max_pool_3_U = nn.MaxPool2d(2)
        
        # for X
        self.conv1_1_X = conv3x3(1, 32)
        self.conv1_2_X = conv3x3(32, 64)
        self.max_pool_1_X = nn.MaxPool2d(2)
        
        self.conv2_1_X = conv3x3(64, 64)
        self.conv2_2_X = conv3x3(64, 128)
        
        self.max_pool_2_X = nn.MaxPool2d(2)
        
        self.conv3_1_X = conv3x3(128, 128)
        self.conv3_2_X = conv3x3(128, 256)
        
        self.max_pool_3_X = nn.MaxPool2d(2)
        
        
        # 16 * 16
            

    def forward(self, image_batch):
        # ouptut size = 256 * 16 * 16 for both
        if type(image_batch) != torch.Tensor:
            image_batch = torch.Tensor(image_batch).cuda()
        U = image_batch[:, shapes['u_space'][0] : shapes['u_space'][1]]
        U = U.view(-1, con['U_channel'], con['U_height'], con['ast_embedding_size'])
        X = image_batch[:, shapes['x_space'][0] : shapes['x_space'][1]]
        X = X.view(-1, 1, con['X_height'], con['ast_embedding_size'])
        u = relu(self.conv1_1_U(U))
        u = relu(self.conv1_2_U(u))
        u = self.max_pool_1_U(u)
        u = relu(self.conv2_1_U(u))
        u = relu(self.conv2_2_U(u))
        u = self.max_pool_1_U(u)
        u = relu(self.conv3_1_U(u))
        u = relu(self.conv3_2_U(u))
        u = self.max_pool_1_U(u)
        x = relu(self.conv1_1_X(X))
        x = relu(self.conv1_2_X(x))
        x = self.max_pool_1_X(x)
        x = relu(self.conv2_1_X(x))
        x = relu(self.conv2_2_X(x))
        x = self.max_pool_1_X(x)
        x = relu(self.conv3_1_X(x))
        x = relu(self.conv3_2_X(x))
        x = self.max_pool_1_X(x)
        u_out = u.view(-1, shapes['u_out_shape'])
        x_out = x.view(-1, shapes['x_out_shape'])
        return torch.cat([u_out, x_out], axis=1)
