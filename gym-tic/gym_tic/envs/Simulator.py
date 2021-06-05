from typing import List
from configs.Configure import state_key_tensors
import numpy as np
import copy

def simulate(ast, slice, actions_history, action):
    path_str = ''
    for act in actions_history:
        path_str += str(act.index + 1)
 
    ast = copy.deepcopy(ast)
    next_state = copy.deepcopy(state_key_tensors[path_str])
    return (ast, next_state)


def break_tensors(ast, slice, actions_history, action):
    path_str = ''
    for act in actions_history:
        path_str += str(act.index + 1)
 
    ast = copy.deepcopy(ast)
    next_state = copy.deepcopy(state_key_tensors[path_str])
    return (ast, next_state)



