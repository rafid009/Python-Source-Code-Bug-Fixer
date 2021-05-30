from preprocessing.ast2vec import Ast2Vec
from utils.utils import *
import os
import json

embedding_model = Ast2Vec('./code2vec.model')

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
    