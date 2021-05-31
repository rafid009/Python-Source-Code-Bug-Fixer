import gym
from gym import error, spaces, utils
from gym.utils import seeding
import os
import random as ran
import numpy as np
import copy
# import Configure as con
from configs.Configure import configuration as con
from configs.Configure import embedding_model
from .specimen_parsers.array_maker import TensorRep
import copy


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


    def _get_specimens(self, file_path):#filepath: file to answer or json
        specimens = {}
        files = os.listdir(file_path)
        for file in files:
            name = file.split("_answers")[0].split(".json")[0]
            if name not in specimens.keys() and (".json" in file or "_answers" in file):
                specimens[name] = {"spec": "", "answer": ""}
            if ".json" in file:
                specimens[name]['spec'] = file
            elif "_answers" in file:
                specimens[name]['answer'] = file
        return specimens

    def get_reachability_map(self):
    
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

            i = 0
            for filename in os.listdir(train_folder):
                if i > 2:
                    break
                json_list = to_string_list(json.loads(open(train_folder+filename).read()))
                slices = processed_dict[filename]['paths']
                print('full ast: ', embedding_model.get_tensor_representaion(json_list).size())
                for key in slices.keys():
                    slice = get_ast_path(slices[key], json_list)
                    print(key, '\n', embedding_model.get_tensor_representaion(slice).size())
                    i += 1

                specimen_path, failure_paths = self._select_specimen()
                array_builder = TensorRep(specimen_path, print_tokens=con['print_tokens'])
                tensors = array_builder.make_tensor()
                if tensors == None:
                    return build_specimen()
                return specimen_path, failure_paths, array_builder, tensors
            # specimen_path, failure_paths = self._select_specimen()
            # array_builder = TensorRep(specimen_path, print_tokens=con['print_tokens'])
            # tensors = array_builder.make_tensor()
            # if tensors == None:
            #     return build_specimen()
            # return specimen_path, failure_paths, array_builder, tensors


        self.specimen_path, self.failure_paths, self.array_builder, self.tensors = build_specimen()


        # self.failure_state = self.get_failure_state(self.failure_path)

        self.counter = 0
        self.done = False
        self.branches_taken = []

        return self.get_state_array()

    def get_reachable_branches(self):
        # Eliminate the negative elements of the adjancency matrix B (we do not need edges ariving at the node.)
        B = np.where(self.tensors['B'] > 0, 1, 0)
        # Obrain the indices of the conditions that are reachable from this node.
        branches = np.nonzero(B[self.current_node])
        # Convert the tuple "branches" into an array.  Ofset it by 1 since the starting branch does not have a
        # corresponding action.

        return np.array(branches, dtype=np.int32)[0]

    def seed(self, seed=1):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def get_failure_state(self, failure_path):
        # failure path is offset by 1.  Initialization condition is condition 0. The first condition is condition 1
        fail_state = copy.deepcopy(self.tensors['U'][:, :, 0, :])
        for condition in failure_path:
            fail_state += self.tensors['U'][:, :, condition, :]
        return fail_state

    def get_state_array(self):


        return np.concatenate((self.tensors['U'].flatten(),
                               self.tensors['B'].flatten(),
                               self.tensors['X'].flatten(),
                               self.tensors['J'].flatten(), #con['vars'], con['max_support']+3
                               self.tensors['K'].flatten())) #con['conditions'], 3

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
            slice = copy.deepcopy(self.tensors['U'][:, :, action.index + 1, :])
            # Add the current move to the state involving all previous moves.
            self.tensors['X'] = self.tensors['X'] + np.expand_dims(slice, 2)

            state_array = self.get_state_array()
            self.counter += 1
        # If There are no nodes reachable by the current node, we have reached the end of the specimen program.
        condition_tensor = np.where(self.tensors['B'] == 1, 1, 0)
        if np.sum(condition_tensor[self.current_node]) == 0:
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

        raw_file = os.path.join(self.file_path, self.specimens[spec_name]['spec'])
        answer_file = os.path.join(self.file_path, self.specimens[spec_name]['answer'])
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
            return raw_file, failure_paths
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

    def render(self, mode='text'):
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
            self.array_builder.render(self.tensors['X'][:, :, 0, :])

    def close(self):
        pass


if __name__ == "__main__":
    file_path = "/Users/arrenbustamante/Documents/BinMorph/MuZero/MuZero Old/gym-tic/gym_tic/envs/specimen_parsers/specimen_raw.py"
    SpecimenEnv(file_path=file_path)
