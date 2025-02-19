import random
from itertools import zip_longest
from typing import List

from configs.config import MuZeroConfig

from game.game import AbstractGame, Action


class ReplayBuffer(object):

    def __init__(self, config: MuZeroConfig):
        self.window_size = config.window_size
        self.batch_size = config.batch_size
        self.buffer = []

    def dump_memory(self):
        self.buffer = []

    def save_game(self, game):
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)
        self.buffer.append(game)

    def sample_batch(self, num_unroll_steps: int, td_steps: int):
        # Generate some sample of data to train on
        games = self.sample_games()
        game_pos = [(g, self.sample_position(g)) for g in games]
        game_data = [(g.make_image(i), g.history[0:i + num_unroll_steps], g.history[i:i + num_unroll_steps],
                      g.make_target(i, num_unroll_steps, td_steps, g.to_play()), g)
                     for (g, i) in game_pos]

        # Pre-process the batch
        image_batch, actions_history, actions_time_batch, targets_batch, games = zip(*game_data)
        # print('image_batch: ', type(image_batch), type(image_batch[0]))
        # print('action hist: ', actions_history, '\naction time batch: ', actions_time_batch)

        #targets_init_batch should be the initial value predicted for each element of the batch.
        targets_init_batch, *targets_time_batch = zip(*targets_batch)
        actions_time_batch = list(zip_longest(*actions_time_batch, fillvalue=None))
        temp_actions_history = list(zip_longest(*actions_history, fillvalue=None))
        # print('temp: ', temp_actions_history)
        # Building batch of valid actions and a dynamic mask for hidden representations during BPTT
        mask_time_batch = []
        dynamic_mask_time_batch = []
        last_mask = [True] * len(image_batch)
        for i, actions_batch in enumerate(actions_time_batch):
            mask = list(map(lambda a: bool(a), actions_batch))
            dynamic_mask = [now for last, now in zip(last_mask, mask) if last]
            mask_time_batch.append(mask)
            dynamic_mask_time_batch.append(dynamic_mask)
            last_mask = mask
            actions_time_batch[i] = [action.index for action in actions_batch if action]

        actions_history = []
        for actions_batch in temp_actions_history:
            for i in range(len(actions_batch)):
                if len(actions_history) <= i:
                    actions_history.append([actions_batch[i].index + 1])
                else:
                    actions_history[i].append(actions_batch[i].index + 1)
        # print("actions hist after: ", actions_history)
        batch = image_batch, targets_init_batch, targets_time_batch, actions_history, actions_time_batch, mask_time_batch, dynamic_mask_time_batch, games
        return batch

    def sample_games(self) -> List[AbstractGame]:
        # Sample game from buffer either uniformly or according to some priority.
        k = min(len(self.buffer), self.batch_size)
        return random.choices(self.buffer, k=k)

    def sample_position(self, game: AbstractGame) -> int:
        # Sample position from game either uniformly or according to some priority.
        return random.randint(0, len(game.history))
