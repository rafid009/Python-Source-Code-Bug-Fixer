import time
from typing import Optional

import numpy as np

def get_current_time_in_millis():
    return int(time.time() * 1000)

def to_string_list(code_list):
    return [str(c) for c in code_list]

MAXIMUM_FLOAT_VALUE = float('inf')


class MinMaxStats(object):
    """A class that holds the min-max values of the tree."""

    def __init__(self, known_bounds):
        self.maximum = known_bounds.max if known_bounds else -MAXIMUM_FLOAT_VALUE
        self.minimum = known_bounds.min if known_bounds else MAXIMUM_FLOAT_VALUE

    def update(self, value: float):
        if value is None:
            raise ValueError

        self.maximum = max(self.maximum, value)
        self.minimum = min(self.minimum, value)

    def normalize(self, value: float) -> float:
        # If the value is unknow, by default we set it to the minimum possible value
        if value is None:
            return 0.0

        if self.maximum > self.minimum:
            # We normalize only when we have set the maximum and minimum values.
            return (value - self.minimum) / (self.maximum - self.minimum)
        return value


class Node(object):
    """A class that represent nodes inside the MCTS tree"""

    def __init__(self, prior: float):
        self.visit_count = 0
        self.to_play = -1
        self.prior = prior
        self.value_sum = 0
        self.children = {}
        self.hidden_state = None
        self.reward = 0

    def expanded(self) -> bool:
        return len(self.children) > 0

    def value(self) -> Optional[float]:
        if self.visit_count == 0:
            return None
        return self.value_sum / self.visit_count
    
    def set_action(self, action):
        self.action = action


def softmax_sample(visit_counts, actions, t):
    counts_exp = np.exp(visit_counts) * (1 / t)
    probs = counts_exp / np.sum(counts_exp, axis=0)
    action_idx = np.random.choice(len(actions), p=probs)
    return actions[action_idx]

def eigen(A):
    """Calculates the the eigenvalues and eigenvectors associated with
    the normalized Laplacian of a given adjacency matrix.
    Inputs:
        A - Adjacecny matrix (must be a square matrix)
    Outputs:
        E - An array of eigenvalues
        V - an array of eigenvectors
            axis0 - each node from the given adjacency matrix
            axis1 - each dimension of the eigenspace occupied by the eigenvector
    """
    # Obtain the distance diagonal of the adjacency matrix
    d = np.sum(A**2,axis=0)
    # Create an identity matrix
    I = np.eye(A.shape[0])

    D = I*d
    # Calculate the Laplacian Matrix
    L = D-A**2

    # Obtain the eigenvalues and eigenvectors of the laplacian
    E, V = np.linalg.eigh(L)
    return E, V


def check_connectivity(A):
    """
    Checks to see if a directed graph is connected by checking the first
    eigenvector of the laplacean.
    """
    a_size = np.argmin(np.sum(A*np.eye(A.shape[0]),1))
    if a_size !=0:
        a = A[:a_size,:a_size]
    else:
        a = A
    E,V = eigen(a)

    try:
        if E[1] >1e-10:
            return True
        else:
            return False
    except IndexError:
        return None
    
def get_index_from_action_history(action_history=[], key=''):
    state_to_index = {
        '0': 0,
        '0-1': 1,
        '0-1-3': 2,
        '0-1-4': 3,
        '0-1-3-5': 4,
        '0-1-4-5': 5,
        '0-2': 6,
        '0-2-3': 7,
        '0-2-4': 8,
        '0-2-3-5': 9,
        '0-2-4-5': 10,
        'ast': 11
    }
    if key == 'ast':
        return state_to_index[key]
    path_str = '0'
    if len(action_history) != 0 and type(action_history[0]) == int:
        for action in action_history:
            path_str += '-' + str(action)
    else:
        for action in action_history:
            path_str += '-' + str(action.index + 1)
    return state_to_index[path_str]

def get_index_from_action_path(path_str='ast'):
    state_to_index = {
        '0': 0,
        '0-1': 1,
        '0-1-3': 2,
        '0-1-4': 3,
        '0-1-3-5': 4,
        '0-1-4-5': 5,
        '0-2': 6,
        '0-2-3': 7,
        '0-2-4': 8,
        '0-2-3-5': 9,
        '0-2-4-5': 10,
        'ast': 11
    }
    return state_to_index[path_str]