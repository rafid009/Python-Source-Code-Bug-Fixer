import json
import os
from preprocessing.ast2vec import Ast2Vec
import numpy as np

json_config = os.path.join(os.getcwd(),'configs/master_config.json')
with open(json_config,'r') as f:
    try:
        configuration = json.load(f)
    except:
        configuration = json.load(f.read())
configuration['U_SIZE'] = configuration['U_channel'] * configuration['U_height'] * configuration['ast_embedding_size']
configuration['X_SIZE'] = configuration['X_height'] * configuration['ast_embedding_size']
configuration['FLAT_SIZE'] = configuration['U_SIZE'] + configuration['X_SIZE']


shapes = {}
shapes['u_out_shape'] = configuration['U_out_channel'] * configuration['U_out_size'] ** 2
shapes['x_out_shape'] = configuration['X_out_channel'] * configuration['X_out_size'] ** 2

shapes['u_in_shape'] = configuration['U_channel'] * configuration['U_height'] * configuration['ast_embedding_size']
shapes['x_in_shape'] = configuration['X_height'] * configuration['ast_embedding_size']


shapes['u_space'] = (0, shapes['u_in_shape'])
shapes['x_space'] = (shapes['u_space'][1], shapes['u_space'][1] + shapes['x_in_shape'])

shapes['u_out_space'] = (0, shapes['u_out_shape'])
shapes['x_out_space'] = (shapes['u_out_space'][1], shapes['u_out_space'][1] + shapes['x_out_shape'])

shapes['observation_size'] = shapes['u_in_shape'] + shapes['x_in_shape']
shapes['output_size'] = shapes['u_out_shape'] + shapes['x_out_shape']


# configuration['raw_file_path'] = configuration['raw_file_path_Arren']
configuration['specimen_test_path'] = configuration['eval_ast_path']
configuration['specimen_train_path'] = configuration['train_ast_path']
configuration['specimen_eval_path'] = configuration['eval_ast_path']


stats = {"win":0, "loss":0}
embedding_model = Ast2Vec('./code2vec.model')
