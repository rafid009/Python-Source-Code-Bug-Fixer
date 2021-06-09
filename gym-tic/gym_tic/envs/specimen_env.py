import gym
from gym import error, spaces, utils
from gym.utils import seeding
import os
import random as ran
import numpy as np
import torch.nn.functional as F
import torch
import copy
# import Configure as con
from configs.Configure import configuration as con
from configs.Configure import embedding_model
from game.game import Action
import copy
from utils.utils import *
import json

class SpecimenEnv(gym.Env):

    def __init__(self, file_path=None, render_this=False):
        # Get a dictionary with specimen[name] = {raw_program:raw_path, answer_key:answer_path}
        self.file_path = file_path
        self.specimens = self._get_specimens(file_path[0], file_path[1], file_path[2])
        self.render_this = render_this
        # Set State spaces
        self.action_space = spaces.Discrete(con['conditions'])
        self.observation_space = spaces.Discrete(con['FLAT_SIZE'])

        self.seed()
        self.viewer = None

        # self.reset()


        self.steps_beyond_done = None
        self.current_node = 0


    def _get_specimens(self, file_path_ast, file_path_answers, file_path_states):#filepath: file to answer or json
        specimens = {}
        files = os.listdir(file_path_ast)
        for file in files:
            name = file.split(".json")[0]
            # print('file: ',file,'\nname: ',name)
            if name not in specimens.keys() and (".json" in file):
                specimens[name] = {"ast": ""}
            if ".json" in file:
                specimens[name]['ast'] = file


        files = os.listdir(file_path_answers)
        for file in files:
            name = file.split("_answers")[0]
            if name not in specimens.keys() and (".json" in file or "_answers" in file):
                specimens[name]['answer'] = ""
            if "_answers" in file:
                specimens[name]['answer'] = file

        files = json.loads(open(file_path_states).read())
        for key in files.keys():
            name = key.split(".json")[0]
            specimens[name]['paths'] = files[key]['paths']
            
        return specimens

    def get_reachability_map(self):
    
        map_dict = {
            0 : [1, 2],
            1 : [3, 4],
            2 : [3, 4],
            3 : [5],
            4 : [5],
            5 : []
        }
        return map_dict

    def reset(self):
        """
        Resets the board to start a new game
        """
        def build_specimen():
            train_folder = self.file_path[0] #'./data/train-asts/'
            processed = self.file_path[2] #'./processed/train-processed.json'
            # processed_dict = json.loads(open(processed).read())

            def get_ast_path(node_list, ast):
                ast_slice = []
                for i in node_list:
                    ast_slice.append(ast[i])
                return ast_slice

            
            specimen_path, failure_paths = self._select_specimen()
            json_list = to_string_list(json.loads(open(specimen_path).read()))
            # print(processed_dict.keys())
            specimen_name = specimen_path.split('/')[-1].split('.json')[0]
            slices = self.specimens[specimen_name]['paths']
            tensors = {}
            ast = embedding_model.get_tensor_representaion(json_list)
            serial = ['0', '0-1', '0-1-3', '0-1-4', '0-1-3-5', '0-1-4-5', '0-2', '0-2-3', '0-2-4', '0-2-3-5', '0-2-4-5', 'ast']
            tensor_states = {'ast': np.reshape(ast, (1, ast.shape[0], ast.shape[1]))}
            for key in slices.keys():
                    slice = get_ast_path(slices[key], json_list)
                    embed = embedding_model.get_tensor_representaion(slice)
                    tensor_states[key] = np.reshape(embed, (1, embed.shape[0], embed.shape[1]))
                    # state_key_tensors[key] = embed
            sub_asts = []
            for key in serial:
                # print('tensor states key: ', type(tensor_states[key]), tensor_states[key].shape)
                resized = F.adaptive_avg_pool2d(torch.from_numpy(tensor_states[key]), (con['U_height'], con['ast_embedding_size']))
                sub_asts.append(resized)
            tensors['U'] = torch.cat(sub_asts, axis=0).numpy()
            # print('in game: U: ', tensors['U'].shape)
            tensors['X'] = sub_asts[0].numpy()
            # print('in game: X: ', tensors['X'].shape)
            return specimen_path, failure_paths, tensors


        self.specimen_path, self.failure_paths, self.tensors = build_specimen()


        # self.failure_state = self.get_failure_state(self.failure_path)

        self.counter = 0
        self.done = False
        self.branches_taken = []

        return self.get_state_array()

    def get_reachable_branches(self):

        map_dict = {
            0 : [1, 2],
            1 : [3, 4],
            2 : [3, 4],
            3 : [5],
            4 : [5],
            5 : []
        }

        return np.array(map_dict[self.current_node], dtype=np.int32)

    def seed(self, seed=1):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def get_failure_state(self, failure_path):
        path_str = '0'

        for i in failure_path:
            path_str = path_str +  '-' + str(i)

        return np.expand_dims(self.tensors['U'][get_index_from_action_path(path_str), :, :], 0)
        


    def get_state_array(self):
        return np.concatenate((self.tensors['U'].flatten(), self.tensors['X'].flatten()))
        

    def check_against_ground(self, actions_taken=[1], failure_paths=[[None]]):
        result = False
        for failure_path in failure_paths:

            for i in range(len(failure_path)):
                if len(actions_taken) == len(failure_path):
                    if failure_path[i] == actions_taken[i]:
                        result = True
                    else:
                        result = False
                        break

                else:
                    result = False
                    break

            if result:
                self.done = True
                # print(self.branches_taken, self.failure_path)
                return con['REWARDS']['win']
        if not result and len(self.get_reachable_branches()) == 0:
            # print(self.branches_taken, self.failure_path)
            self.done = True
            return con['REWARDS']['loss']
        return 0.0


    def step(self, action: Action):
        if not self.done:
            self.branches_taken.append(action.index + 1)
            # Take slice of U to represent the current move.
            action_index = get_index_from_action_history(self.branches_taken)
            slice = copy.deepcopy(self.tensors['U'][action_index, :, :])
            self.tensors['X'] = self.tensors['X'] + np.expand_dims(slice, 0)
            # Add the current move to the state involving all previous moves.

            state_array = self.get_state_array()
            self.counter += 1

        # If There are no nodes reachable by the current node, we have reached the end of the specimen program.
        if (action.index + 1) ==  5:
            self.done = True

        # Actions are zero indexed while nodes are 1 indexed.
        self.current_node = action.index + 1
        reward = self.check_against_ground(actions_taken=self.branches_taken, failure_paths=self.failure_paths)

        return state_array, reward, self.done, {}

    def _select_specimen(self):

        spec_list = list(self.specimens.keys())
        rand_num = ran.randint(0, len(self.specimens) - 1)
        spec_name = spec_list[rand_num]
        # spec_name = 'spec5994'
        # print(spec_name)

        raw_file = os.path.join(self.file_path[0], self.specimens[spec_name]['ast'])
        # print('raw_file: ', raw_file)
        answer_file = os.path.join(self.file_path[1], self.specimens[spec_name]['answer'])
        if os.path.exists(raw_file) and self.specimens[spec_name]['answer'] != '':
            with open(answer_file, 'r') as f:
                answers = f.read()

            # Convert the string in "answers" to a numpy array containing the path needed to get to the goal "failure" state.
            failure_paths = []
            for answer in answers.split("\n"):
                answer = answer.replace("[",'').replace("]",'')
                if len(answer) > 0:
                    failure_path = np.array([int(a.strip()) for a in answer.split(",")]).astype(np.int32)
                    failure_paths.append(failure_path)
            return raw_file, failure_paths
        else:
            return self._select_specimen()

    def render(self, mode='text', initial_node=False):
        """
        Draws the board to the screen
        """
        
        if self.render_this:
            # In order to account for a null element, the argmax is multiplied by the sum along the f axis so that
            # zeros in the sum will eliminate elements that are supposed to be blank.
            # The operations dictionary is also offset by 1 so that a value of 0 gives the null element.
            # print("Actions taken:")
            # print(self.branches_taken)
            # print("Correct actions:")
            # print(self.failure_path)
            
            return self.tensors['X']

    def close(self):
        pass