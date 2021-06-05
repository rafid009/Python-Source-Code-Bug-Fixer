import pickle
import numpy as np
from configs.Configure import configuration as con
import torch
import torch.nn.functional as F
import os


class Recorder:
    def __init__(self, save_path=None):
        if not save_path:
            save_path = self.get_save_path()
        self.file_path = self.get_record_path(save_path)
        self.state = {'representation':[],
                      'value':[],
                      'policy':[],
                      'dynamic':[],
                      'reward':[]}
        self.target ={'representation':[],
                      'value':[],
                      'policy':[],
                      'dynamic':[],
                      'reward':[]}
        self.losses = {'policy':[],
                       'value':[],
                       'reward':[],
                       'l2':[]}

    def get_record_path(self, save_path):
        recorder_path = os.path.join(save_path,'records')
        if not os.path.exists(recorder_path):
            os.mkdir(recorder_path)

        records = [item for item in os.listdir(recorder_path) if 'record' in item]

        record_number = (len(records)+1)*con['record_every']
        next_record = "record " + str(record_number) + ".pkl"

        record_path = os.path.join(recorder_path, next_record)
        return record_path

    def get_save_path(self):
        weight_path = con['save_path']
        models = [item for item in os.listdir(weight_path) if 'model' in item]
        return os.path.join(weight_path,models[-1])


    def add_representation(self, rep, target_rep):
        self.state['representation'].append((np.array(rep[0]), np.array(rep[1])))
        self.target['representation'].append((np.array(target_rep[0]), np.array(target_rep[1])))

    def add_reward(self, reward, target_reward):
        self.state['reward'].append(np.array(reward))
        self.target['reward'].append(np.array(target_reward))

    def add_value(self, value, target_value):
        self.state['value'].append(np.array(F.softmax(value)))
        self.target['value'].append(np.array(self.loss_value(target_value)))

    def add_policy(self, policy, target_policy):
        self.state['policy'].append(np.array(F.softmax(policy)))
        self.target['policy'].append(np.array(target_policy))

    def add_dynamic(self, dynamic, target_dynamic):
        self.state['dynamic'].append(np.array(dynamic))
        self.target['dynamic'].append(np.array(target_dynamic))

    def add_reward(self, reward, target_reward):
        self.state['reward'].append(np.array(reward))
        self.target['reward'].append(np.array(target_reward))

    def add_losses(self, policy=None, value=None, reward=None, l2=None):
        self.losses['policy'].append(policy)
        self.losses['value'].append(value)
        self.losses['reward'].append(reward)
        self.losses['l2'].append(l2)

    def loss_value(self,target_value_batch):
        target_value_batch = torch.from_numpy(np.array(target_value_batch).astype(np.float32))
        epsilon = 1e-4
        target_pos = torch.from_numpy(target_value_batch)
        target_zer = torch.from_numpy(torch.abs(target_value_batch) < epsilon, 1.0, 0.0)
        target_neg = F.relu(-target_value_batch)

        targets = torch.stack((target_neg,target_zer, target_pos),1)

        return targets

    def compile(self):
        output = {'targets':self.target, 'states':self.state, 'config':con}
        with open(self.file_path,'wb') as g:
            pickle.dump(output,g)
        print('recorded')
