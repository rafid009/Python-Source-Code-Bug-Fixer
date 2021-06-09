"""Training module: this is where MuZero neurons are trained."""

from models.default_network import DefaultNetwork
from typing import Dict
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
import torch.nn as nn

from configs.config import MuZeroConfig
from models.models import BaseNetwork
from shared_storage.shared_storage import SharedStorage

from training.replay_buffer import ReplayBuffer
from models.recorder import Recorder
from configs.Configure import configuration as con
from gym_tic.envs.Simulator import simulate
import logging

def train_network(config: MuZeroConfig, storage: SharedStorage, replay_buffer: ReplayBuffer, epochs: int, loop:int):
    network = storage.current_network
    optimizer_info = storage.optimizer_info
    network.loop = loop
    for i in range(epochs):
        batch = replay_buffer.sample_batch(config.num_unroll_steps, config.td_steps)
        if i == 0:
            network.record_this = storage.record_this
        print('before update weights')
        update_weights(optimizer_info, network, batch)
        print('after update weights')
        storage.save_network(network.training_steps, network)
        storage.record_this = network.record_this



def update_weights(optimizer_info: Dict, network: DefaultNetwork, batch):

    def scale_gradient(tensor, scale: float):
        """Trick function to scale the gradient in tensorflow"""
        return (1. - scale) * torch.Tensor.detach(tensor) + scale * tensor
    def L2(weights):
        alpha = con['spectral_weight_decay']
        l2 = 0
        for weight in weights:
            l2+= alpha* abs(torch.sum(weight ** 2))
        return l2

    def calulate_value_loss(value_batch=None, target_value_batch=None):

        batch_size = len(target_value_batch)
        targets = torch.zeros(batch_size, 4).cuda()
        floor_value = torch.floor(target_value_batch).type(torch.LongTensor).cuda()
        rest = target_value_batch - floor_value
        targets[range(batch_size), floor_value+1] = 1 - rest
        targets[range(batch_size), floor_value + 2] = rest
        targets = targets[:,0:3]
        # print('value: ',value_batch.dtype, '\ntarget: ', targets.dtype)
        value_loss = F.binary_cross_entropy_with_logits(value_batch, targets)
        return value_loss #torch.mean(value_loss)

    def calculate_policy_loss(policy_batch=None, target_policy_batch=None):
        p = policy_batch
        pi = target_policy_batch

        zero = torch.zeros(list(pi.size()), dtype=torch.float32).cuda()
        where = torch.eq(pi, zero).cuda()

        negatives = torch.full(pi.shape, -100.0).cuda()
        p = torch.where(where, negatives, p).cuda()

        loss = F.binary_cross_entropy_with_logits(p, pi)

        return loss #torch.mean(loss)


    def loss():
        image_batch, targets_init_batch, targets_time_batch, actions_history, actions_time_batch, mask_time_batch, dynamic_mask_time_batch, games0 = batch
        image_batch_tensor = torch.as_tensor(image_batch, dtype=torch.float32)
        # Initial step, from the real observation: representation + prediction networks
        value_batch, policy_batch = network.initial_model(Variable(image_batch_tensor).cuda())

        # Only update the element with a policy target
        target_value_batch, target_reward_batch1, target_policy_batch = zip(*targets_init_batch)
        mask_policy = list(map(lambda l: bool(l), target_policy_batch))
        target_policy_batch = list(filter(lambda l: bool(l), target_policy_batch))
        policy_batch = policy_batch[torch.as_tensor(mask_policy)==True, :] #torch.masked_select(policy_batch, torch.as_tensor(mask_policy).cuda())



        if network.record_this:
            convolved_image = network.representation_network(Variable(image_batch_tensor).cuda())
            recorder = Recorder()
            recorder.add_representation(image_batch, convolved_image)
            recorder.add_value(torch.squeeze(value_batch), target_value_batch)
            recorder.add_policy(policy_batch, target_policy_batch)

        # Compute the loss of the first pass
        target_policy_batch = torch.as_tensor(target_policy_batch).cuda()
        target_value_batch = torch.as_tensor(target_value_batch, dtype=torch.float32).cuda()

        value_loss = calulate_value_loss(value_batch=value_batch, target_value_batch=target_value_batch)
        policy_loss = calculate_policy_loss(policy_batch=policy_batch, target_policy_batch=target_policy_batch)
        reward_loss = 0.0
        # Recurrent steps, from action and previous hidden state.
        i = -1
        print('before loss calc loop')
        print(zip(targets_time_batch, mask_time_batch, dynamic_mask_time_batch))
        print('sizes: ', len(targets_time_batch), '\n', mask_time_batch, dynamic_mask_time_batch)
        actions_history_batch = actions_history
        for targets_batch, mask, dynamic_mask in zip(targets_time_batch,
                                                                    mask_time_batch, dynamic_mask_time_batch):
            print('inside loss calc loop')
            target_value_batch, target_reward_batch2, target_policy_batch = zip(*targets_batch)
            i +=1
            # print('dyn mask: ', torch.as_tensor(dynamic_mask).shape, '\nmask: ', torch.as_tensor(mask).shape, '\nbatch: ', len(image_batch))
            # Only execute BPTT for elements with an action
            # print("dynamic: ", dynamic_mask)
            # print("img batch before: ", type(image_batch), torch.Tensor(image_batch).shape,'\n',image_batch)
            image_batch = torch.as_tensor(image_batch)[torch.as_tensor(dynamic_mask)==True, :] #torch.masked_select(image_batch, dynamic_mask)
            # print('img batch: ', image_batch.shape)
            target_reward_batch1 = target_reward_batch1[mask==True] #torch.masked_select(target_reward_batch1, mask)

            games1 = [games0[g] for g in range(len(games0)) if dynamic_mask[g]]
            target_value_batch = target_value_batch[mask==True] #torch.masked_select(target_value_batch, mask)
            # Creating conditioned_representation: concatenate representations with actions batch
            # actions_batch = F.one_hot(actions_batch, network.action_size)

            image1 = simulate(image_batch, actions_history_batch[0:len(image_batch)])
            # Recurrent step from conditioned representation: recurrent + prediction networks
            value_batch, reward_batch, policy_batch = network.recurrent_model(Variable(image1).cuda())
            print('values: ', value_batch)
            print('rewards: ',reward_batch)
            print('policies: ', policy_batch)
            # Only execute BPTT for elements with a policy target
            target_policy_batch = [policy for policy, b in zip(target_policy_batch, mask) if b]
            mask_policy = list(map(lambda l: bool(l), target_policy_batch))
            target_policy_batch = torch.as_tensor([policy for policy in target_policy_batch if policy]).cuda()
            policy_batch = policy_batch[torch.as_tensor(mask_policy)==True, :] #torch.masked_select(policy_batch, mask_policy).cuda()


            #TODO: Figure out why this happens and Come up with a more robust fix for this later
            if policy_batch.shape[0] == 0:
                policy_batch = torch.zeros((1, policy_batch.shape[1]), dtype=torch.float32).cuda()
                target_policy_batch = torch.zeros((1, policy_batch.shape[1]), dtype=torch.float32).cuda()


            if network.record_this and i == 0:
                recorder.add_policy(policy_batch,target_policy_batch)
                recorder.add_representation(image1, network.representation_network(image1))
                recorder.add_value(torch.squeeze(value_batch), target_value_batch)
                recorder.add_reward(reward_batch,target_reward_batch1)
                recorder.compile()
                network.record_this = False
                print("stop recording")

            # Compute the partial loss

            value_l = calulate_value_loss(value_batch=value_batch, target_value_batch=target_value_batch)
            policy_l = calculate_policy_loss(policy_batch=policy_batch, target_policy_batch=target_policy_batch)


            target_reward_batch1 = F.relu(target_reward_batch1)
            reward_batch = reward_batch[:,0]

            reward_l = F.binary_cross_entropy_with_logits(reward_batch, target_reward_batch1)
            # reward_l = tf.losses.mean_absolute_error(y_true=target_reward_batch1, y_pred=tf.nn.sigmoid(reward_batch))
            # reward_l = torch.mean(reward_l)
            # print("reward loss:", round(float(reward_loss),3))


            # Scale the gradient of the loss by the average number of actions unrolled
            gradient_scale = 1. / len(actions_time_batch)

            policy_loss += scale_gradient(policy_l,gradient_scale)
            value_loss += scale_gradient(value_l,gradient_scale)
            reward_loss += scale_gradient(reward_l,gradient_scale)

            games0 = games1
            image_batch = image1
            target_reward_batch1 = target_reward_batch2

        l2_loss = L2(network.representation_network.parameters())

        if network.loop < con['start_reward_train']:
            loss = reward_loss
        else:
            loss = policy_loss + value_loss + reward_loss + l2_loss
        loss_string = "value: " + str(round(float(value_loss),3)) + " policy: " + str(round(float(policy_loss),3)) + \
              " reward: " + str(round(float(reward_loss),3))
        logging.info(loss_string)
        print('after loss calc loop')
        print(loss_string)
        return loss
    optimizer = optim.Adam(network.cb_get_variables(), lr=optimizer_info['lr'])
    optimizer.zero_grad()
    print('before loss function')
    loss = loss()
    print('after loss function')
    loss.backward()
    optimizer.step()
    network.training_steps += 1


