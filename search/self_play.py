"""Self-Play module: where the games are played."""
import torch
from configs.config import MuZeroConfig
from game.game import AbstractGame
from models.models import AbstractNetwork
from shared_storage.shared_storage import SharedStorage
from search.mcts import run_mcts, select_action, expand_node, add_exploration_noise
from training.replay_buffer import ReplayBuffer
from configs.Configure import configuration as con
import numpy as np
import os
from utils.utils import *
from gevent.pool import Pool


class Thread:
    def __init__(self, network, config, replay_buffer, render, train_episodes, mode=None):
        self.network = network
        self.pool = Pool(con['pool_workers'])
        self.config = config
        self.replay_buffer = replay_buffer
        self.render = render
        self.train_episodes = train_episodes
        self.returns = []
        self.mode = mode
        self.game_sort = []
    def task(self):
        if self.mode == 'self_play':
            self.game_sort = None
            game = play_game(self.config, self.network, train=True, render_this=self.render)
            self.replay_buffer.save_game(game)
            self.returns.append(sum(game.rewards))


            game.env.close()
        elif self.mode == "eval":
            game = play_game(self.config, self.network, train=False, render_this=self.render)

            rewards = sum(game.rewards)

            # game.connectivity_mat = np.sign(np.sum(game.env.tensors['X'][:, :, 0] ** 2, -1))
            # game.graph_is_connected = check_connectivity(game.connectivity_mat)
            game.graph_is_connected = True
            # vis.add_game(game)

            game_file = os.path.split(game.env.specimen_path)[1]
            self.returns.append(rewards)
            self.game_sort.append((game_file, rewards, game.graph_is_connected))
            game.env.close()

    def run(self):
        for i in range(self.train_episodes):
            self.pool.spawn(self.task)
        self.pool.join()
        return self.returns, self.game_sort


def _check_win_loss(returns):
    stats = {"win":0,"tie":0,"loss":0}
    for game in returns:
        if game == con['REWARDS']['win']:
            stats['win'] += 1
        elif game == con['REWARDS']['tie']:
            stats['tie'] += 1
        elif game == con['REWARDS']['loss']:
            stats['loss'] +=1
    return stats


def run_selfplay(config: MuZeroConfig, storage: SharedStorage, replay_buffer: ReplayBuffer, train_episodes: int, render: bool):
    """Take the latest network, produces multiple games and save them in the shared replay buffer"""
    network = storage.latest_network()

    T = Thread(network, config, replay_buffer, render, train_episodes,mode='self_play')
    returns, game_sort = T.run()

    return sum(returns) / train_episodes, game_sort


def run_eval(config: MuZeroConfig, storage: SharedStorage, eval_episodes: int, render=False, plot=False, weight_path=None):
    """Evaluate MuZero without noise added to the prior of the root and without softmax action selection"""
    network = storage.latest_network()
    # vis.add_network(network, weight_path)
    T = Thread(network, config, None, render, eval_episodes, mode='eval')
    returns, game_sort = T.run()

    stats = _check_win_loss(returns)
    # if plot:
    #     vis.make_plots()
    return sum(returns) / eval_episodes, game_sort, (stats if eval_episodes else 0,0)


def play_game(config: MuZeroConfig, network: AbstractNetwork, train: bool = True, render_this=False) -> AbstractGame:
    """
    Each game is produced by starting at the initial board position, then
    repeatedly executing a Monte Carlo Tree Search to generate moves until the end
    of the game is reached.
    """
    game = config.new_game()
    game.render_this = render_this
    game.env.render_this = render_this

    #Random agent is used for model comparisons
    if con['random_agent']:
        mode_action_select = "random"
    else:
        mode_action_select = 'softmax' if train else 'max'
    # game.env.reset()

    while not game.terminal() and len(game.history) < config.max_moves:
        # At the root of the search tree we use the representation function to
        # obtain a hidden state given the current observation.
        root = Node(0)
        raw_current_observation = np.expand_dims(game.make_image(-1),0) 
        # current_observation = network.pre_con_network.run(convert_to_tensor(raw_current_observation))
        expand_node(root, game.to_play(), game.legal_actions(), network.initial_inference(raw_current_observation))

        if train:
            add_exploration_noise(config, root)

        # We then run a Monte Carlo Tree Search using only action sequences and the
        # model learned by the networks.
        reachability = game.env.get_reachability_map()
        run_mcts(config, root, game.action_history(), network, reachability)
        action = select_action(config, len(game.history), root, network, mode=mode_action_select)
        game.apply(action)
        if render_this and game.done:
            game.env.render()

        game.store_search_statistics(root)
    return game



