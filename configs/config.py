import collections
from typing import Optional, Dict

from game.game import AbstractGame

from gym_tic.envs.specimen_wrapper import SpecimenWrapper
from models.default_network import DefaultNetwork
from models.models import BaseNetwork, UniformNetwork
from configs.Configure import configuration as con

KnownBounds = collections.namedtuple('KnownBounds', ['min', 'max'])

import os
class MuZeroConfig(object):

    def __init__(self,
                 game,
                 nb_training_loop: int,
                 nb_episodes: int,
                 nb_epochs: int,
                 network_args: Dict,
                 network,
                 action_space_size: int,
                 max_moves: int,
                 discount: float,
                 dirichlet_alpha: float,
                 num_simulations: int,
                 batch_size: int,
                 td_steps: int,
                 unroll_steps: int,
                 pb_init: int,
                 visit_softmax_temperature_fn,
                 lr: float,
                 known_bounds: Optional[KnownBounds] = None,
                 oponent=None,
                 specimen_path=None):
        ### Environment
        self.game = game
        self.oponent =oponent
        self.specimen_path = specimen_path

        ### Self-Play
        self.action_space_size = action_space_size
        # self.num_actors = num_actors

        self.visit_softmax_temperature_fn = visit_softmax_temperature_fn
        self.max_moves = max_moves
        self.num_simulations = num_simulations
        self.discount = discount

        # Root prior exploration noise.
        self.root_dirichlet_alpha = dirichlet_alpha
        self.root_exploration_fraction = 0.25

        # UCB formula
        self.pb_c_base = con['pb_c_base']#19652
        self.pb_c_init = pb_init

        # If we already have some information about which values occur in the
        # environment, we can use them to initialize the rescaling.
        # This is not strictly necessary, but establishes identical behaviour to
        # AlphaZero in board games.
        self.known_bounds = known_bounds

        ### Training
        self.nb_training_loop = nb_training_loop
        self.nb_episodes = nb_episodes  # Nb of episodes per training loop
        self.nb_epochs = nb_epochs  # Nb of epochs per training loop

        # self.training_steps = int(1000e3)
        # self.checkpoint_interval = int(1e3)
        self.window_size = int(1e6)
        self.batch_size = batch_size
        self.num_unroll_steps = unroll_steps
        self.td_steps = td_steps

        self.weight_decay = 1e-4
        self.momentum = 0.9

        self.network_args = network_args
        self.network = network
        self.lr = lr
        # Exponential learning rate schedule
        # self.lr_init = lr_init
        # self.lr_decay_rate = 0.1
        # self.lr_decay_steps = lr_decay_steps

    def new_game(self) -> AbstractGame:
        game =  self.game(self.discount, self.specimen_path)
        return game

    def new_network(self) -> BaseNetwork:
        return self.network(**self.network_args).cuda()

    def uniform_network(self) -> UniformNetwork:
        return UniformNetwork(self.action_space_size).cuda()

    def new_optimizer(self) -> Dict:
        # return tf.keras.optimizers.SGD(learning_rate=self.lr, momentum=self.momentum)
        if con['continue_training']:
            import pickle
            with open(os.path.join(con['load_path'], 'optimizer.pkl'),'rb') as f:
                optimizer = pickle.load(f)
        else:
            optimizer = {'type': 'adam', 'lr': self.lr}#tf.keras.optimizers.Adam(learning_rate=self.lr, clipvalue=1.0)
        return optimizer



def make_config() -> MuZeroConfig:
    def visit_softmax_temperature(num_moves, training_steps):
        return 1.0

    return MuZeroConfig(
        game=SpecimenWrapper,
        nb_training_loop=con['loops'],
        nb_episodes=con['episodes'],
        nb_epochs=con['epochs'],
        network_args={'action_size': con['conditions']},
        network=DefaultNetwork,
        action_space_size=con['conditions'],
        max_moves=con['max_moves'],
        discount=con['discount'],
        dirichlet_alpha=con['alpha'],
        num_simulations=con['simulations'],  # Odd number perform better in eval mode
        batch_size=con['batch_size'],
        td_steps=con['td_steps'],
        unroll_steps=con['unroll_steps'],
        visit_softmax_temperature_fn=visit_softmax_temperature,
        lr=con['lr'],
        pb_init=con['pb_c_init'],
        oponent=None,
        specimen_path=con['specimen_train_path'])

def playtest_config() -> MuZeroConfig:
    def visit_softmax_temperature(num_moves, training_steps):
        return 1.0

    return MuZeroConfig(
        game=SpecimenWrapper,
        nb_training_loop=con['loops'],
        nb_episodes=con['episodes'],
        nb_epochs=con['epochs'],
        network_args={'action_size': con['conditions']},
        network=DefaultNetwork,
        action_space_size=con['conditions'],
        max_moves=con['max_moves'],
        discount=con['discount'],
        dirichlet_alpha=con['eval_alpha'],
        num_simulations=con['simulations'],  # Odd number perform better in eval mode
        batch_size=con['batch_size'],
        td_steps=con['td_steps'],
        unroll_steps=con['unroll_steps'],
        visit_softmax_temperature_fn=visit_softmax_temperature,
        lr=con['lr'],
        pb_init=con['pb_c_init_eval'],
        oponent=None,
        specimen_path=con['specimen_eval_path'])

