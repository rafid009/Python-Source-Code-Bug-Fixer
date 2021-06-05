from typing import List

# from .gamesFolder import gym
import gym
from game.game import Action, AbstractGame
from game.game_wrappers import ScalingObservationWrapper
from gym import wrappers, logger
# from .specimen_parsers import game_config
from configs.Configure import configuration as con
import numpy as np
from copy import deepcopy

class SpecimenWrapper(AbstractGame):

    def __init__(self, discount: float, file_path):
        super().__init__(discount)
        self.env = gym.make('specimen_env-v0', file_path=file_path)
        # self.env = ScalingObservationWrapper(self.env)
        # Actions are 0 indexed while reachable branches are 1 indexed (Branch 0 is the initialization state)
        self.actions = list(map(lambda i: Action(i), range(con['conditions'])))
        self.observations = [self.env.reset()]
        self.done = False

    @property
    def action_space_size(self) -> int:
        """Return the size of the action space."""
        return len(self.actions)

    def step(self, action) -> int:
        """Execute one step of the game conditioned by the given action."""
        observation, reward, done, _ = self.env.step(action)

        self.observations += [observation]
        self.done = done

        return reward

    def terminal(self) -> bool:
        """Is the game is finished?"""
        return self.done

    def legal_actions(self) -> List[Action]:
        """Return the legal actions available at this instant."""
        #Actions are zero indexed while branches are 1 indexed.
            #This is due to the fact that branch 0 is the initialization node.
        reachable_branches = self.env.get_reachable_branches()-1
        valid_actions = []
        for action in self.actions:
            if action.index in reachable_branches:
                valid_actions.append(action)

        return valid_actions

    def make_image(self, state_index: int):
        """Compute the state of the game."""
        return self.observations[state_index].astype(np.float32)

