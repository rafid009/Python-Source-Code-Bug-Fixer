import math

import numpy as np
import torch
# from game.game import Action
from models.models import BaseNetwork
import os
import json
import pickle

# from networks.spectral import eigen, laplacean
from configs.Configure import configuration as con
# from gym_tic.envs.specimen_parsers.Configure import shapes as S

from numpy.random import seed

seed(1)

def conv3x3(in_channels, out_channels, stride=1, padding=1):
    return torch.nn.Conv2d(
        in_channels, out_channels, kernel_size=3, stride=stride, padding=padding, bias=False
    )

def adaptiveAvgPool(shape):
    return torch.nn.AdaptiveAvgPool2d(shape)

def adaptiveMaxPool(shape):
    return torch.nn.AdaptiveMaxPool2d(shape)

def relu(x):
    return torch.nn.functional.relu(x)

class DefaultNetwork(BaseNetwork):

    def __init__(self,
                 weight_decay: float = 1e-4,
                 action_size: int = 0,
                 state_size: int = 0,
                 load_path: str = None):

        # regularizer = regularizers.l2(weight_decay)
        if con['continue_training']:
            load_path = con['load_path']
        
        self.policy_network = None
        self.value_network = None
        self.reward_network = None 
        self.representation_network = None
        self.meta_data = None
        if load_path:
            self.policy_network, self.value_network, self.reward_network, self.representation_network, self.meta_data = self.load_networks(load_path)
            self.action_size = self.meta_data['action_size']
        else:
            self.action_size = action_size

            self.representation_network = RepresentationNetwork()
            
            input_features = 512 * 16 * 16
            
            self.value_network = torch.nn.Sequential(
                torch.nn.Linear(input_features, con['hidden_value']),
                torch.nn.SELU(),
                torch.nn.Linear(con['hidden_value'], 3)
            )
            
            self.reward_network = torch.nn.Sequential(
                torch.nn.Linear(input_features, con['hidden_reward']),
                torch.nn.SELU(),
                torch.nn.Linear(con['hidden_reward'], 1)
            )
            
            self.reward_network = torch.nn.Sequential(
                torch.nn.Linear(input_features, con['hidden_policy']),
                torch.nn.SELU(),
                torch.nn.Linear(con['hidden_policy'], action_size)
            )
            
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


        super().__init__(self.value_network, self.reward_network, self.policy_network, self.representation_network, load_path=load_path)

    def load_networks(self, file_path='./saved-models'):
        self.policy_network = torch.load(os.path.join(file_path, 'policy_network.pb'))
        self.value_network = torch.load(os.path.join(file_path, 'value_network.pb'))
        self.reward_network = torch.load(os.path.join(file_path, 'reward_network.pb'))
        self.representation_network = torch.load(os.path.join(file_path, "representation_network.pkl"))

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
    
    def _conditioned_hidden_state(self, hidden_state: np.array, action: Action) -> np.array:
        conditioned_hidden = np.concatenate((hidden_state, np.eye(self.action_size)[action.index]))
        return np.expand_dims(conditioned_hidden, axis=0)

    def _softmax(self, values):
        """Compute softmax using numerical stability tricks."""
        values_exp = np.exp(values - np.max(values))
        return values_exp / np.sum(values_exp)


class RepresentationNetwork(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # variable size
        self.conv1_init1 = conv3x3(1, 32)
        self.conv2_init1 = conv3x3(32, 64)
        self.adap_avg_pool1 = adaptiveAvgPool((con['input_fixed_rep_height'], con['input_fixed_rep_width']))
        # 64 * 64
        
        # variable size
        self.conv1_init2 = conv3x3(1, 32)
        self.conv2_init2 = conv3x3(32, 64)
        self.adap_avg_pool2 = adaptiveAvgPool((con['input_fixed_rep_height'], con['input_fixed_rep_width']))
        # 64 * 64
        
        # 64 * 64
        self.conv2_1 = conv3x3(128, 128)
        self.conv2_2 = conv3x3(128, 256)
        self.max_pool2 = torch.nn.MaxPool2d(2)
        # 32 * 32
        
        # 32 * 32
        self.conv3_1 = conv3x3(256, 256)
        self.conv3_2 = conv3x3(256, 512)
        self.max_pool3 = torch.nn.MaxPool2d(2)
        # 16 * 16
        
        # 64 * 64
        self.conv3_1_init2 = conv3x3(128, 128)
        self.conv3_2_init2 = conv3x3(128, 256)
        self.max_pool2_init2 = torch.nn.MaxPool2d(2)
        # 32 * 32
        
        # 32 * 32
        self.conv4_1_init2 = conv3x3(256, 256)
        self.conv4_2_init2 = conv3x3(256, 512)
        self.max_pool3_init2 = torch.nn.MaxPool2d(2)
        # 16 * 16
            

    def forward(self, x1, x2):
        # ouptut size = 512 * 16 * 16 for both
        e1 = relu(self.conv1_init1(x1))
        e1 = relu(self.conv2_init1(e1))
        e1 = self.adap_avg_pool1(e1)
        
        e2 = relu(self.conv1_init2(x2))
        e2 = relu(self.conv2_init2(e2))
        e2 = self.adap_avg_pool2(e2)
        
        e = torch.cat((e1, e2), 1)
        
        y1 = relu(self.conv2_1(e))
        y1 = relu(self.conv2_2(y1))
        y1 = self.max_pool2(y1)
        
        y1 = relu(self.conv3_1(y1))
        y1 = relu(self.conv3_2(y1))
        y1 = self.max_pool3(y1)
        
        y2 = relu(self.conv3_1_init2(e2))
        y2 = relu(self.conv3_2_init2(y2))
        y2 = self.max_pool2_init2(y2)
        
        y2 = relu(self.conv4_1_init2(y2))
        y2 = relu(self.conv4_2_init2(y2))
        y2 = self.max_pool3_init2(y2)
        
        return y1.view(-1, 512 * 16 * 16), y2.view(-1, 512 * 16 *16)
