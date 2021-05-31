# from gym_tic.envs.tic_env import TicEnv
from copy import deepcopy as dc
import numpy as np

def check_legality(board, space_int):
    # space_int -= 1
    one_hot_space = np.zeros(9, dtype=np.int32)
    one_hot_space[space_int] = 1

    space = one_hot_space.reshape((3, 3, 1))

    space_check = np.sum(space * board)
    if space_check == 1:
        return False
    else:
        return True

def _check_condition(row):
    if np.sum(row) == 3:
        return True
    else:
        return False


def _check_diagonals(board, player):
    players_board =board[:, :, player]
    diag1 = np.eye(3, dtype=np.int32)
    diag2 = diag1[::-1]
    for diag in [diag1, diag2]:
        sum = np.sum(diag * players_board)
        if sum == 3:
            return True
    return False

def move_space(_board, player, space):
    board = dc(_board)
    one_hot_space = np.zeros(9, dtype=np.int32)
    one_hot_space[space] = 1
    board[:, :, player] += one_hot_space.reshape((3, 3))
    return board

def check_win_conditions(board, player):
    for i in range(3):

        row = _check_condition(board[:, i, player])
        column = _check_condition(board[i, :, player])
        diagonal = _check_diagonals(board, player)
        if row or column or diagonal:
            return True
    return False

def check_wins(player,_board):
    board = dc(_board)
    for i in range(0,8):
        if check_legality(board, i):
            hypothetical = move_space(board, player, i)
            winning_move = check_win_conditions(hypothetical, player)
            if winning_move:
                return i
    return None

def get_corner(board):
    legal_corners = []
    for i in [0,2,6,8]:
        if check_legality(board, i):
            legal_corners.append(i)
    if len(legal_corners) > 0:
        return legal_corners[0]
    else:
        return None

def get_a_space(board):
    legal_spaces = []
    for i in [1,3,4,5,7]:
        if check_legality(board, i):
            legal_spaces.append(i)
    return legal_spaces[0]

def master_agent(master_board):
    board = dc(master_board)
    move = check_wins(1,board)
    if move == None:
        move = check_wins(0, board)
    if move == None:
        move = get_corner(board)
    if move == None:
        move = get_a_space(board)
    return move

if __name__== "__main__":
    cpu = [[1,0,0],
           [0,0,1],
           [1,0,1]]
    agent = [[0,0,1],
           [1,1,0],
           [0,0,0]]

    cpu = np.expand_dims(np.array(cpu),-1)
    agent = np.expand_dims(np.array(agent),-1)

    master_board = np.concatenate((cpu,agent),-1)
    move = master_agent(master_board)
    print(move)








