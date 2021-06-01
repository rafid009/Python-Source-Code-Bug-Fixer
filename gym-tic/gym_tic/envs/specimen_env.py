import gym
from gym import error, spaces, utils
from gym.utils import seeding
import os
import random as ran
import numpy as np
import copy
# import Configure as con
from configs.Configure import configuration as con
from configs.Configure import state_tensors_key, state_key_tensors
from configs.Configure import embedding_model
from .specimen_parsers.array_maker import TensorRep
import copy
from utils.utils import *
import json

class SpecimenEnv(gym.Env):

    def __init__(self, file_path=None, render_this=False):
        # Get a dictionary with specimen[name] = {raw_program:raw_path, answer_key:answer_path}
        self.file_path = file_path
        self.specimens = self._get_specimens(file_path)

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

        files = os.listdir(file_path_states)
        for key, file in files:
            name = key.split("_answers")[0].split(".json")[0]
            if name not in specimens.keys() and (".json" in file):
                specimens[name]['states'] = ''
            if ".json" in file:
                specimens[name]['states'] = files[key]
            
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
        B = np.where(self.tensors['B'] > 0, 1, 0)
        map_dict = {}
        for node in range(B.shape[0]):
            branches = np.nonzero(B[node])[0]
            map_dict[node] = branches.tolist()
        return map_dict

    def reset(self):
        """
        Resets the board to start a new game
        """
        def build_specimen():
            train_folder = './data/train-asts/'
            processed = './processed/train-processed.json'
            processed_dict = json.loads(open(processed).read())

            def get_ast_path(node_list, ast):
                ast_slice = []
                for i in node_list:
                    ast_slice.append(ast[i])
                return ast_slice

            
            specimen_path, failure_paths, state_paths = self._select_specimen()
            json_list = to_string_list(json.loads(open(train_folder+specimen_path).read()))
            slices = processed_dict[specimen_path]['paths']
            
            tensors_ast = embedding_model.get_tensor_representaion(json_list)
            
            tensor_states = {}
            for key in slices.keys():
                    slice = get_ast_path(slices[key], json_list)
                    embed = embedding_model.get_tensor_representaion(slice)
                    tensor_states[key] = embed
                    state_tensors_key[embed] = key
               

            state_key_tensors = tensor_states

            return specimen_path, failure_paths, tensors_ast, tensor_states


        self.specimen_path, self.failure_paths, self.tensors_ast, self.tensors_states = build_specimen()


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

        return np.array(map_dict[self.current_node], dtype=np.int32)[0]

    def seed(self, seed=1):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def get_failure_state(self, failure_path):
        path_str = ''

        for i in failure_path:
            path_str = path_str + str(i) + '-'
        path_str = path_str[:-1]

        return self.tensor_states[path_str]
        


    def get_state_array(self):

        return (self.tensors_ast, self.tensors_states)
        

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


    def step(self, action):
        if not self.done:
            self.branches_taken.append(action.index + 1)
            # Take slice of U to represent the current move.
            
            path_str = ''

            for i in self.branches_taken:
                path_str = path_str + str(i) + '-'
            path_str = path_str[:-1]
            
            slice = copy.deepcopy(self.self.tensor_states[path_str])

            # Add the current move to the state involving all previous moves.
            # self.tensors['X'] = self.tensors['X'] + np.expand_dims(slice, 2)

            state_array = self.get_state_array()
            self.counter += 1

        # If There are no nodes reachable by the current node, we have reached the end of the specimen program.
        condition_tensor = np.where(self.tensors['B'] == 1, 1, 0)
        if action.index ==  4:
            self.done = True

        # Actions are zero indexed while nodes are 1 indexed.
        self.current_node = action.index + 1

        reward = self.check_against_ground(actions_taken=self.branches_taken, failure_paths=self.failure_paths)

        # self.array_builder.render(self.tensors['U'][:, :, 0, :])

        return state_array, reward, self.done, {}

    def _select_specimen(self):

        spec_list = list(self.specimens.keys())
        rand_num = ran.randint(0, len(self.specimens) - 1)
        spec_name = spec_list[rand_num]
        # spec_name = 'spec5994'
        # print(spec_name)

        raw_file = os.path.join(self.file_path, self.specimens[spec_name]['ast'])
        answer_file = os.path.join(self.file_path, self.specimens[spec_name]['answer'])
        state_file = os.path.join(self.file_path, self.specimens[spec_name]['answer'])
        if os.path.exists(raw_file) and self.specimens[spec_name]['answer'] != '':
            with open(answer_file, 'r') as f:
                answers = f.read()

            # Convert the string in "answers" to a numpy array containing the path needed to get to the goal "failure" state.
            failure_paths = []
            for answer in answers.split("\n"):
                answer = answer.replace("[",'').replace("]",'')
                if len(answer) > 0:
                    failure_path = np.array([a.strip() for a in answer.split(",")]).astype(np.int32)
                    failure_paths.append(failure_path)
            return raw_file, failure_paths, state_file
        else:
            return self._select_specimen()

    def reset(self):
        """
        Resets the board to start a new game
        """
        def build_specimen():
            specimen_path, failure_paths = self._select_specimen()
            array_builder = TensorRep(specimen_path, print_tokens=con['print_tokens'])
            tensors = array_builder.make_tensor()
            if tensors == None:
                return build_specimen()
            return specimen_path, failure_paths, array_builder, tensors

        self.specimen_path, self.failure_paths, self.array_builder, self.tensors = build_specimen()


        # self.failure_state = self.get_failure_state(self.failure_path)

        self.counter = 0
        self.done = False
        self.branches_taken = []

        return self.get_state_array()

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

            if initial_node = True:
                return (self.tensors_ast, self.tensors_states['0'])
            
            path_str = ''

            for i in self.branches_taken:
                path_str = path_str + str(i) + '-'
            path_str = path_str[:-1]
            
            return (self.tensors_ast, self.tensors_states[path_str])


    def close(self):
        pass
