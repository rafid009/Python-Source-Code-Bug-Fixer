import typing
from abc import ABC, abstractmethod
from typing import Dict, List, Callable
import numpy as np
import torch
import torch.nn as nn
from game.game import Action
import os
from gym_tic.envs.Simulator import simulate, break_tensors

class NetworkOutput(typing.NamedTuple):
    value: float
    reward: float
    policy_logits: Dict[Action, float]
    hidden_state: typing.Optional[List[float]]

    @staticmethod
    def build_policy_logits(policy_logits):
        return {Action(i): logit for i, logit in enumerate(policy_logits[0])}

class AbstractNetwork(ABC):

    def __init__(self):
        self.training_steps = 0

    @abstractmethod
    def initial_inference(self, image) -> NetworkOutput:
        pass

    @abstractmethod
    def recurrent_inference(self, hidden_state, action) -> NetworkOutput:
        pass


class UniformNetwork(AbstractNetwork):
    """policy -> uniform, value -> 0, reward -> 0"""

    def __init__(self, action_size: int):
        super().__init__()
        self.action_size = action_size

    def initial_inference(self, image) -> NetworkOutput:
        return NetworkOutput(0, None, {Action(i): 1 / self.action_size for i in range(self.action_size)}, None)

    def recurrent_inference(self, hidden_state, action) -> NetworkOutput:
        return NetworkOutput(0,0, {Action(i): 1 / self.action_size for i in range(self.action_size)}, None)


class InitialModel(torch.nn.Module):
    """Model that combine the representation and prediction (value+policy) network."""

    def __init__(self, value_network: nn.Module, policy_network: nn.Module, representation_network):
        super(InitialModel, self).__init__()
        self.value_network = value_network
        self.policy_network = policy_network
        self.representation_network = representation_network

    def forward(self, all_state_image, curr_state_image):
        all_curr_encoding, curr_state_encoding = self.representation_network(all_state_image, curr_state_image)
        value = self.value_network(all_curr_encoding)
        policy_logits = self.policy_network(all_curr_encoding)
        return value, policy_logits


class RecurrentModel(torch.nn.Module):
    """Model that combine the dynamic, reward and prediction (value+policy) network."""

    def __init__(self,value_network: nn.Module, reward_network: nn.Module, policy_network: nn.Module, representation_network):
        super(RecurrentModel, self).__init__()
        self.value_network = value_network
        self.reward_network = reward_network
        self.policy_network = policy_network
        self.representation_network = representation_network

    def forward(self, all_state_image, curr_state_image):
        all_curr_encoding, curr_state_encoding = self.representation_network(all_state_image, curr_state_image)
        value = self.value_network(all_curr_encoding)
        reward = self.reward_network(curr_state_encoding)
        policy_logits = self.policy_network(all_curr_encoding)
        return value, reward, policy_logits


class BaseNetwork(AbstractNetwork):
    """Base class that contains all the networks and models of MuZero."""

    def __init__(self, value_network: nn.Module, reward_network: nn.Module, policy_network: nn.Module, representation_network=None, load_path: str=None):
        super().__init__()
        # Networks blocks
        self.value_network = value_network
        self.reward_network = reward_network
        self.policy_network = policy_network
        self.representation_network = representation_network
        # Models for inference and training
        self.initial_model = InitialModel(self.value_network, self.policy_network, self.representation_network)
        self.recurrent_model = RecurrentModel(self.value_network, self.reward_network, self.policy_network, self.representation_network)

    def save_networks(self,file_path='./saved-models'):
        torch.save(self.policy_network, os.path.join(file_path,'policy_network.pth'))
        torch.save(self.value_network, os.path.join(file_path,'value_network.pth'))
        torch.save(self.reward_network, os.path.join(file_path, 'reward_network.pth'))
        torch.save(self.representation_network, os.path.join(file_path, 'representation_network.pth'))
        print("Saved model")

    def initial_inference(self, image) -> NetworkOutput:
        """representation + prediction function"""
        value, policy_logits = self.initial_model(image)
        output = NetworkOutput(value=self._value_transform(value),
                               reward=0,
                               policy_logits=NetworkOutput.build_policy_logits(policy_logits),
                               hidden_state=image)
        return output

    def recurrent_inference(self, input_state: np.array, action: Action) -> NetworkOutput:
        """dynamics + prediction function"""
        new_state = simulate(input_state,action.index+1)
        value, reward, policy_logits = self.recurrent_model.predict(new_state)
        output = NetworkOutput(value=self._value_transform(value),
                               reward=0,
                               policy_logits=NetworkOutput.build_policy_logits(policy_logits),
                               hidden_state=new_state)
        return output

    @abstractmethod
    def _value_transform(self, value: np.array) -> float:
        pass

    @abstractmethod
    def _reward_transform(self, reward: np.array) -> float:
        pass

    @abstractmethod
    def _conditioned_hidden_state(self, hidden_state: np.array, action: Action) -> np.array:
        pass

    def cb_get_variables(self) -> Callable:
        """Return a callback that return the trainable variables of the network."""
        def get_variables():
            networks = (self.value_network, self.policy_network, self.reward_network, self.representation_network)
            return [variables
                    for variables_list in map(lambda n: n.weights, networks)
                    for variables in variables_list]
        return get_variables
