import math

import numpy as np
import torch
# from game.game import Action
from models.models import BaseNetwork
import os
import json
import pickle

# from networks.spectral import eigen, laplacean
# from gym_tic.envs.specimen_parsers.Configure import configuration as con
# from gym_tic.envs.specimen_parsers.Configure import shapes as S

from numpy.random import seed

seed(1)

def weight_init(fanin, type='he'):
    """He Xavier variance calculation for initialization
    Inputs:
        fanin - (int) The number of input inputs to a given layer.
    Returns: An integer corresponding to the needed variance to initialize the trainable variable."""
    if type=='he':
        return np.sqrt(2 / fanin)
    if type=='selu':
        return np.sqrt(1 / fanin)

class DefaultNetwork(BaseNetwork):

    def __init__(self,
                 weight_decay: float = 1e-4,
                 action_size: int = 0,
                 state_size: int = 0,
                 load_path: str = None):

        regularizer = regularizers.l2(weight_decay)
        if con['continue_training']:
            load_path = con['load_path']

        if load_path:
            policy_network, value_network, reward_network, pre_con_network, meta_data = self.load_networks(load_path)
            self.action_size = meta_data['action_size']
        else:
            self.action_size = action_size
            shapes = S

            value_network = Sequential([Dense(con['hidden_value'], activation='selu', kernel_regularizer=regularizer,
                                              kernel_initializer='lecun_normal', bias_initializer="lecun_normal",
                                              input_dim=shapes['output_size']),
                                        Dense(3, kernel_regularizer=regularizer, input_dim=con['hidden_value'])])

            reward_network = Sequential([Dense(con['hidden_reward'], activation='selu', kernel_regularizer=regularizer,
                                              kernel_initializer='lecun_normal', bias_initializer="lecun_normal",
                                               input_dim=(shapes['x_out_shape'])),
                                        Dense(1, kernel_regularizer=regularizer, input_dim=con['hidden_reward'],
                                              activation=None)])

            policy_network = Sequential([Dense(con['hidden_policy'], activation='selu', kernel_regularizer=regularizer,
                                               kernel_initializer='lecun_normal', bias_initializer="lecun_normal",
                                               input_dim=shapes['output_size']),
                                         Dense(action_size, kernel_regularizer=regularizer,
                                               input_dim=con['hidden_policy'])])

            pre_con_network = PreConvolve(file_path=load_path, load_from_path=False, shapes=shapes)

        super().__init__(value_network, reward_network, policy_network, pre_con_network, load_path=load_path)

    def load_networks(self, file_path='test'):
        policy_network = tf.keras.models.load_model(os.path.join(file_path, 'policy_network.pb'))
        value_network = tf.keras.models.load_model(os.path.join(file_path, 'value_network.pb'))
        reward_network = tf.keras.models.load_model(os.path.join(file_path, 'reward_network.pb'))
        pre_con_network = PreConvolve(os.path.join(file_path, "pre_con_network.pkl"), load_from_path=True)

        with open(os.path.join(file_path,'meta_data.json'),'r') as g:
            meta_data = json.load(g)

        print("loaded model")
        return policy_network, value_network, reward_network, pre_con_network, meta_data

    def save_networks(self,file_path='test'):
        self.policy_network.save(os.path.join(file_path,'policy_network.pb'), include_optimizer=False)
        self.value_network.save(os.path.join(file_path,'value_network.pb'), include_optimizer=False)
        self.reward_network.save(os.path.join(file_path, 'reward_network.pb'), include_optimizer=False)
        self.pre_con_network.save(os.path.join(file_path, 'pre_con_network.pkl'))

        meta_data = {'action_size': self.action_size,
                     'training_steps': self.training_steps}

        with open(os.path.join(file_path, 'meta_data.json'),'w') as g:
            json.dump(meta_data,g)


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

#Full spectral convolution.
class PreConvolve:
    def __init__(self,
                 file_path=None,
                 load_from_path=False,
                 shapes=None):
        self.shapes = shapes

        if load_from_path:
            self.load(file_path)
        else:

            self.k = con['k']
            #Calculate the shapes of the trainable variables using the dictionary from the configuration.
            WA_shape = np.array([con['filters'],con['conv_in_embedd'],con['con_embedding_dim']])
            WB_shape = np.array([con['filters'],3,con['con_embedding_dim']])

            WC_shape = np.array([con['operations'],con['filters']])
            WO_shape = np.array([con['filters'],con['con_embedding_dim'],con['final_embedding']])

            C_shape = np.array([con['final_embedding'], self.k])
            #Make trainable variables
            self.WA_U = self.make_var(WA_shape)
            self.WA_BU = self.make_var(WA_shape)
            self.WA_BB = self.make_var(WB_shape)

            self.WC_U = self.make_var(WC_shape)
            self.WO_U = self.make_var(WO_shape)
            self.WC_B = self.make_var(WC_shape)
            self.WO_B = self.make_var(WO_shape)

            self.WA_X = self.make_var(WA_shape)
            self.WC_X = self.make_var(WC_shape)
            self.WO_X = self.make_var(WO_shape)

            self.C_K = self.make_var(C_shape)
            self.C_Q = self.make_var(C_shape)
            self.C_V = self.make_var(C_shape)

            #Make a list of all trainable variables
            self.weights = [self.WA_U, self.WA_BU, self.WA_BB,self.WC_U, self.WO_U, self.WC_B, self.WO_B,
                            self.WA_X, self.WC_X, self.WO_X, self.C_K, self.C_Q, self.C_V]

    def make_var(self,shape, load=None):
        if type(load) == np.ndarray:
            return tf.Variable(load, dtype=tf.float32)
        else:
            return tf.Variable(np.random.normal(0, self.He(np.product(shape)), shape), dtype=tf.float32)



    def He(self,fanin):
        """He Xavier variance calculation for initialization
        Inputs:
            fanin - (int) The number of input inputs to a given layer.
        Returns: An integer corresponding to the needed variance to initialize the trainable variable."""
        return np.sqrt(2 / fanin)

    def load(self, file_path):
        with open(file_path,'rb') as f:
            in_dict = pickle.load(f)

        #Calculate shapes
        self.k = con['k']
        WA_shape = np.array([con['filters'],con['conv_in_embedd'],con['con_embedding_dim']])
        WC_shape = np.array([con['operations'],con['filters']])
        WO_shape = np.array([con['filters'],con['con_embedding_dim'],con['final_embedding']])
        C_shape = np.array([con['final_embedding'], self.k])

        #Load each variable
        self.WA_U = self.make_var(WA_shape, in_dict[0])
        self.WA_BU = self.make_var(WA_shape, in_dict[1])
        self.WA_BB = self.make_var(WA_shape, in_dict[2])

        self.WC_U = self.make_var(WC_shape, in_dict[3])
        self.WO_U = self.make_var(WO_shape, in_dict[4])
        self.WC_B = self.make_var(WC_shape, in_dict[5])
        self.WO_B = self.make_var(WO_shape, in_dict[6])

        self.WA_X = self.make_var(WA_shape, in_dict[7])
        self.WC_X = self.make_var(WC_shape, in_dict[8])
        self.WO_X = self.make_var(WO_shape, in_dict[9])

        self.C_K = self.make_var(C_shape, in_dict[10])
        self.C_Q = self.make_var(C_shape, in_dict[11])
        self.C_V = self.make_var(C_shape, in_dict[12])

        self.weights = [self.WA_U, self.WA_BU, self.WA_BB, self.WC_U, self.WO_U, self.WC_B, self.WO_B,
                        self.WA_X, self.WC_X, self.WO_X, self.C_K, self.C_Q, self.C_V]

    def save(self, file_path):
        out_dict = {}
        for i in range(len(self.weights)):
            out_dict[i] = np.array(self.weights[i].value())
        with open(file_path,'wb') as g:
            pickle.dump(out_dict,g)

    def B_convolution(self, U,J,B, K):
        step1U = tf.einsum('tnd,mde->tnme',J,self.WA_BU)
        y1U = tf.einsum('tnqco,tqme->tncoe',U,step1U)

        step1B = tf.einsum('tcf,rfg->tcrg',K,self.WA_BB)
        y1B = tf.einsum('tcq,tqrg->tc', B, step1B)

        B_con = tf.einsum('tncoe,tc->tnoe',y1U,y1B)

        y2 = tf.einsum('tnoe,of->tnfe',B_con,self.WC_B)
        y3 = tf.einsum('tnfe,fep->tnp',y2,self.WO_B)
        return y3

    def feastnet_tensor(self, U,J):
        """
        J - (t,n,d)
        U - (t,n,n',c,o)
        """
        if U.shape[3] == 1:
            WA = self.WA_X
            WC = self.WC_X
            WO = self.WO_X
        else:
            WA = self.WA_U
            WC = self.WC_U
            WO = self.WO_U
        step1 = tf.einsum('tnd,mde->tnme',J,WA)
        y1 = tf.einsum('tnqco,tqme->tncoe',U,step1)
        y2 = tf.einsum('tncoe,of->tncfe',y1,WC)
        y3 = tf.einsum('tncfe,fep->tncp',y2,WO)

        K = tf.einsum('tncp, pk -> tnck', y3, self.C_K)
        Q = tf.einsum('tncp, pk -> tnck', y3, self.C_Q)
        V = tf.einsum('tncp, pk -> tnck', y3, self.C_V)

        # preparing the mask

        m_temp = tf.reduce_sum(J[:,:,0:2],-1) 
        inf = tf.scalar_mul(-con['infinity'], tf.ones_like(m_temp))
        m = tf.where(m_temp == 0, inf, m_temp)
        # mask prepared

        q_k = tf.einsum('tnck, tmck -> tncm', Q, K)
        a_nc = tf.nn.softmax(tf.einsum('tncm, tn -> tncm', q_k, m) / (self.k ** 0.5), 3)
        s_nk = tf.einsum('tncm, tmck -> tnck', a_nc, V)

        return tf.nn.leaky_relu(s_nk)

    def run(self,batch):

        VARS = con['vars']
        CONDITIONS = con['conditions']
        OPERATIONS = con['operations']

        U = batch[:,S['u_space'][0] : S['u_space'][1]]
        U = tf.reshape(U,((-1, VARS,VARS, CONDITIONS + 1, OPERATIONS)))

        B = batch[:,S['b_space'][0] : S['b_space'][1]]
        B = tf.reshape(B,(-1,CONDITIONS+1, CONDITIONS+1))

        X = batch[:,S['x_space'][0] : S['x_space'][1]]
        X = tf.reshape(X,(-1, VARS,VARS, OPERATIONS))
        X = tf.expand_dims(X,3)

        J = batch[:,S['J_space'][0]: S['J_space'][1]]
        J = tf.reshape(J,(-1,con['vars'],con['conv_in_embedd']))

        K = batch[:,S['K_space'][0]: S['K_space'][1]]
        K = tf.reshape(K, (-1, con['conditions']+1,3))

        U_out = self.feastnet_tensor(U,J)
        X_out = self.feastnet_tensor(X,J)
        B_out = self.B_convolution(U,J,B,K)
        # B_out = B

        U_out = tf.reshape(U_out,(-1, S['u_out_shape']))
        X_out = tf.reshape(X_out, (-1, S['x_out_shape']))
        B_out = tf.reshape(B_out, (-1, S['b_out_shape']))

        return tf.concat((U_out, B_out,X_out),1)

# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
# pca = PCA(n_components=2)
# y = pca.fit_transform(x)
# plt.scatter(y[:,0],y[:,1])
# plt.show()