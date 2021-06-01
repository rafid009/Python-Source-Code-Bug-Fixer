from gym_tic.envs.specimen_parsers.Configure import configuration as con
import tensorflow_core as tf
import numpy as np
import copy

from configs.Configure import state_tensors_key, state_key_tensors


def simulate(ast, slice, action):

    path_str = state_tensors_key[slice]
    path_str += str(action)

    next_state = state_key_tensors[path_str]
    return (ast, next_state)


def break_tensors(ast, slice, action):

    path_str = state_tensors_key[slice]
    path_str += str(action)

    next_state = state_key_tensors[path_str]
    return (ast, next_state)



