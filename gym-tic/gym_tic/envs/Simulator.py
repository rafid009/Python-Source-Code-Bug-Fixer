from typing import List
from configs.Configure import configuration as con
import numpy as np
import torch
import copy
from utils.utils import *

def simulate(image, actions):   
    U_shape = (-1, con['U_channel'], con['U_height'], con['ast_embedding_size'])
    X_shape = (-1, 1, con['X_height'], con['ast_embedding_size'])

    U_size = -np.prod(U_shape)
    X_size = -np.prod(X_shape)
    if type(image) == np.ndarray:
        image = torch.as_tensor(image)
    U = copy.deepcopy(image[:, 0:U_size])
    X = image[:, U_size:]
    
    U = U.view(U_shape)
    X = X.view(X_shape)
    next_state = 0
    if type(actions[0]) == int:
        # print('actions: ', actions)
        path_str = '0'
        path_str += '-' + '-'.join(np.array(actions).astype(str))
        next_state = U[:, get_index_from_action_path(path_str), :, :]
    else:
        slices =  []
        path_str = '0'
        i = 0
        # print('actions batch: ', actions)
        for acts in actions:
            path_str += '-' + '-'.join((np.array(acts)).astype(str))
            next_slice = U[i, get_index_from_action_path(path_str), :, :]
            slices.append(next_slice)
            i += 1
            path_str = '0'
        next_state = torch.stack(slices, 0)
    X += torch.unsqueeze(next_state, 1)
    U = U.view(-1, U_size)
    X = X.view(-1, X_size)
    return torch.cat([U, X], 1)


def break_tensors(image):
    U_shape = (-1, con['U_channel'], con['U_height'], con['ast_embedding_size'])
    X_shape = (-1, 1, con['X_height'], con['ast_embedding_size'])

    U_size = -np.prod(U_shape)
    X_size = -np.prod(X_shape)
    U = copy.deepcopy(image[:, 0:U_size])
    X = image[:, U_size:]
    return {"U": U, "X": X}



