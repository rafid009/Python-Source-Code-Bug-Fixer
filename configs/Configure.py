import json
import os
import numpy as np
# try:
json_config = os.path.join(os.getcwd(),'configs/master_config.json')
with open(json_config,'r') as f:
    try:
        configuration = json.load(f)
    except:
        configuration = json.load(f.read())
# except FileNotFoundError:
#     json_config = os.path.join(os.getcwd(),r'\Users\dispe\Desktop\InferLink\muZero\muzero\Algorithm\master_config.json')
#     with open(json_config,'r') as f:
#         configuration = json.load(f)

configuration['U_SIZE'] = configuration['vars']**2 * (configuration['conditions']+1) * configuration['op_embedding_dim1']
configuration['B_SIZE'] = (configuration['conditions']+1)**2
configuration['X_SIZE'] = configuration['vars']**2*configuration['op_embedding_dim1']
configuration['FLAT_SIZE'] = configuration['U_SIZE']+configuration['B_SIZE']+configuration['X_SIZE']

configuration['max_support'] = int(np.sqrt(configuration["max_J"] + 1)) + 1
configuration['conv_in_embedd'] = configuration['max_support'] + 3

shapes = {}
shapes['u_out_shape'] = configuration['vars'] * (configuration['conditions'] + 1) * configuration['k']
shapes['b_out_shape'] = configuration['vars'] * configuration['final_embedding']
shapes['x_out_shape'] = configuration['vars'] * configuration['k']

shapes['u_in_shape'] = configuration['vars'] ** 2 * (configuration['conditions'] + 1) * configuration['operations']
shapes['x_in_shape'] = configuration['vars'] ** 2 * configuration['operations']
shapes['b_in_shape'] = (configuration['conditions'] + 1) ** 2
shapes['J_in_shape'] = configuration['vars']*configuration['conv_in_embedd']
shapes['K_in_shape'] = (configuration['conditions']+1) * 3

shapes['u_space'] = (0, shapes['u_in_shape'])
shapes['b_space'] = (shapes['u_space'][1], shapes['u_space'][1] + shapes['b_in_shape'])
shapes['x_space'] = (shapes['b_space'][1], shapes['b_space'][1] + shapes['x_in_shape'])
shapes['J_space'] = (shapes['x_space'][1], shapes['x_space'][1] + shapes['J_in_shape'])
shapes['K_space'] = shapes['J_space'][1], shapes['J_space'][1] + shapes['K_in_shape']

shapes['u_out_space'] = (0, shapes['u_out_shape'])
shapes['b_out_space'] = (shapes['u_out_space'][1], shapes['u_out_space'][1] + shapes['b_out_shape'])

shapes['x_out_space'] = (shapes['b_out_space'][1], shapes['b_out_space'][1] + shapes['x_out_shape'])

shapes['observation_size'] = shapes['u_in_shape'] + shapes['x_in_shape'] + shapes['b_in_shape']
shapes['output_size'] = shapes['u_out_shape'] + shapes['x_out_shape'] + shapes['b_out_shape']

if configuration['AWS']:
    configuration['raw_file_path'] = configuration['raw_file_path_AWS']
    configuration['specimen_train_path'] = configuration['specimen_train_path_AWS']
    configuration['specimen_eval_path'] = configuration['specimen_eval_path_AWS']

    configuration['save_path'] = configuration['save_path_AWS']
    configuration['load_path'] = configuration['load_path_AWS']

else:
    configuration['raw_file_path'] = configuration['raw_file_path_Arren']
    configuration['specimen_test_path'] = configuration['specimen_test_path_Arren']
    configuration['specimen_train_path'] = configuration['specimen_train_path_Arren']
    configuration['specimen_eval_path'] = configuration['specimen_eval_path_Arren']

    configuration['save_path'] = configuration['save_path_Arren']
    configuration['load_path'] = configuration['load_path_Arren']



