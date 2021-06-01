"""Training module: this is where MuZero neurons are trained."""

from typing import Dict
import numpy as np
import torch
import torch.nn.functional as F
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
    # network.loop = loop
    for i in range(epochs):
        batch = replay_buffer.sample_batch(config.num_unroll_steps, config.td_steps)
        # if i == 0:
            # network.record_this = storage.record_this
        update_weights(optimizer_info, network, batch)
        storage.save_network(network.training_steps, network)
        # storage.record_this = network.record_this



def update_weights(optimizer_info: Dict, network: BaseNetwork, batch):

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
        targets = np.zeros((batch_size, 4))
        # This is normally not abs

        # target_value_batch =abs(np.array(target_value_batch))
        # sqrt_value = np.sqrt(target_value_batch)
        floor_value = np.floor(target_value_batch).astype(int)

        # floor_value = np.floor(target_value_batch).astype(int)
        rest = target_value_batch - floor_value
        targets[range(batch_size), floor_value.astype(int)+1] = 1 - rest
        targets[range(batch_size), floor_value.astype(int) + 2] = rest
        targets = targets[:,0:3]


        value_loss = F.cross_entropy(value_batch, targets)
        # value_loss_boosted = (2 + targets)[:, 2] * value_loss
        return torch.mean(value_loss)
        # epsilon = 1e-6
        # target_value_batch = tf.convert_to_tensor(np.array(target_value_batch).astype(np.float32))
        #
        # target_pos = tf.nn.relu(target_value_batch)
        # target_zer = tf.where(tf.abs(target_value_batch) < epsilon, 1.0, 0.0)
        # target_neg = tf.nn.relu(-target_value_batch)
        #
        # targets = tf.stack((target_neg,target_zer, target_pos),1)
        #
        # #boost
        # value_loss = tf.nn.softmax_cross_entropy_with_logits(labels=targets, logits=value_batch)
        # # value_loss_boosted = tf.expand_dims((1+targets)[:,2],-1)* value_loss
        #
        # return tf.reduce_mean(value_loss)

    def calculate_policy_loss(policy_batch=None, target_policy_batch=None):
        # policy_mask = tf.nn.relu(target_policy_batch)
        # policy_loss = tf.reduce_sum(-target_policy_batch * tf.nn.log_softmax(tf.nn.relu(policy_mask*policy_batch)),-1)
        # policy_loss = tf.reduce_mean(policy_loss)
        # policy_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=target_policy_batch, logits=policy_batch))
        # print("policy loss:", round(float(policy_loss),3), "value loss", round(float(value_loss),3))
        # policy_loss = tf.reduce_mean(
        #     tf.nn.softmax_cross_entropy_with_logits(labels=target_policy_batch, logits=policy_batch))

        # p = tf.nn.softmax(policy_batch)
        # policy_loss = -target_policy_batch * tf.keras.backend.log(p)
        # return tf.reduce_mean(policy_loss)

        p = policy_batch
        pi = target_policy_batch

        zero = torch.zeros(shape=pi.shape, dtype=torch.float32)
        where = torch.eq(pi, zero)

        negatives = torch.full(pi.shape, -100.0)
        p = torch.where(where, negatives, p)

        loss = F.cross_entropy(labels=pi, logits=p)

        return torch.mean(loss)


    def loss():
        image_batch, targets_init_batch, targets_time_batch, actions_time_batch, mask_time_batch, dynamic_mask_time_batch, games0 = batch


        # Initial step, from the real observation: representation + prediction networks
        value_batch, policy_batch = network.initial_model(np.array(image_batch))

        # Only update the element with a policy target
        target_value_batch, target_reward_batch1, target_policy_batch = zip(*targets_init_batch)
        mask_policy = list(map(lambda l: bool(l), target_policy_batch))
        target_policy_batch = list(filter(lambda l: bool(l), target_policy_batch))
        policy_batch = torch.masked_select(policy_batch, mask_policy)



        if network.record_this:
            convolved_image = network.representation_network(torch.from_numpy(np.array(image_batch[0]).astype(np.float32)), torch.from_numpy(np.array(image_batch[1]).astype(np.float32)))
            recorder = Recorder()
            recorder.add_representation(image_batch, convolved_image)
            recorder.add_value(torch.squeeze(value_batch), target_value_batch)
            recorder.add_policy(policy_batch, target_policy_batch)

        # Compute the loss of the first pass
        target_policy_batch = torch.from_numpy(target_policy_batch)
        target_value_batch = torch.from_numpy(np.array(target_value_batch).astype(np.float32))

        value_loss = calulate_value_loss(value_batch=value_batch, target_value_batch=target_value_batch)
        policy_loss = calculate_policy_loss(policy_batch=policy_batch, target_policy_batch=target_policy_batch)
        reward_loss = 0.0
        # Recurrent steps, from action and previous hidden state.
        i = -1
        for actions_batch, targets_batch, mask, dynamic_mask in zip(actions_time_batch, targets_time_batch,
                                                                    mask_time_batch, dynamic_mask_time_batch):
            target_value_batch, target_reward_batch2, target_policy_batch = zip(*targets_batch)
            i +=1

            # Only execute BPTT for elements with an action
            image_batch = torch.masked_select(image_batch, dynamic_mask)
            target_reward_batch1 = torch.masked_select(target_reward_batch1, mask)

            games1 = [games0[g] for g in range(len(games0)) if dynamic_mask[g]]
            target_value_batch = torch.masked_select(target_value_batch, mask)
            # Creating conditioned_representation: concatenate representations with actions batch
            actions_batch = F.one_hot(actions_batch, network.action_size)

            image1 = simulate(image_batch, actions_batch)
            # Recurrent step from conditioned representation: recurrent + prediction networks
            value_batch, reward_batch, policy_batch = network.recurrent_model(image1)

            # Only execute BPTT for elements with a policy target
            target_policy_batch = [policy for policy, b in zip(target_policy_batch, mask) if b]
            mask_policy = list(map(lambda l: bool(l), target_policy_batch))
            target_policy_batch = torch.from_numpy([policy for policy in target_policy_batch if policy])
            policy_batch = torch.masked_select(policy_batch, mask_policy)


            #TODO: Figure out why this happens and Come up with a more robust fix for this later
            if policy_batch.shape[0] == 0:
                policy_batch = torch.zeros((1, policy_batch.shape[1]), dtype=torch.float32)
                target_policy_batch = torch.zeros((1, policy_batch.shape[1]), dtype=torch.float32)


            if network.record_this and i == 0:
                recorder.add_policy(policy_batch,target_policy_batch)
                recorder.add_representation(image1, network.representation_network(image1[0], image1[1]))
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

            reward_l = F.cross_entropy(reward_batch, target_reward_batch1)
            # reward_l = tf.losses.mean_absolute_error(y_true=target_reward_batch1, y_pred=tf.nn.sigmoid(reward_batch))
            reward_l = torch.mean(reward_l)
            # print("reward loss:", round(float(reward_loss),3))


            # Scale the gradient of the loss by the average number of actions unrolled
            gradient_scale = 1. / len(actions_time_batch)

            policy_loss += scale_gradient(policy_l,gradient_scale)
            value_loss += scale_gradient(value_l,gradient_scale)
            reward_loss += scale_gradient(reward_l,gradient_scale)

            games0 = games1
            image_batch = image1
            target_reward_batch1 = target_reward_batch2

        l2_loss = L2(network.representation_network.weights)

        if network.loop < con['start_reward_train']:
            loss = reward_loss
        else:
            loss = policy_loss + value_loss + reward_loss + l2_loss
        loss_string = "value: " + str(round(float(value_loss),3)) + " policy: " + str(round(float(policy_loss),3)) + \
              " reward: " + str(round(float(reward_loss),3))
        logging.info(loss_string)
        print(loss_string)
        return loss
    optimizer.minimize(loss=loss, var_list=network.cb_get_variables())
    network.training_steps += 1


