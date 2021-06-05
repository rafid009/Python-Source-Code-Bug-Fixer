from preprocessing.ast2vec import Ast2Vec
from utils.utils import *
import os
import json

# embedding_model = Ast2Vec('./code2vec.model')

train_folder = './data/train-asts/'
processed = './processed/train-processed.json'
processed_dict = json.loads(open(processed).read())

def get_ast_path(node_list, ast):
    ast_slice = []
    for i in node_list:
        ast_slice.append(ast[i])
    return ast_slice

i = 0
max_f = 0
min_f = 999999
max_s = 0
min_s = 999999
# for filename in os.listdir(train_folder):
#     # if i > 2:
#     #     break
#     json_list = to_string_list(json.loads(open(train_folder+filename).read()))
#     slices = processed_dict[filename]['paths']
#     size = list(embedding_model.get_tensor_representaion(json_list).size())[0]
#     if size > max_f:
#         max_f = size
#     if size < min_f:
#         min_f = size
#     # print('full ast: ', size)

#     for key in slices.keys():
#         slice = get_ast_path(slices[key], json_list)
#         slice_size = list(embedding_model.get_tensor_representaion(slice).size())[0]
#         if slice_size > max_s:
#             max_s = slice_size
#         if slice_size < min_s:
#             min_s = slice_size
        # i += 1
print("maximum f size: ", max_f)
print("minimum f size: ", min_f)
print("maximum s size: ", max_s)
print("minimum s size: ", min_s)
    