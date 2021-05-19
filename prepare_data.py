import os
import sys
from typing import Type
import pandas as pd
import numpy as np
import ast #import parse
import json
import ast2json

directory_name = {'eval': '../SE/eval/', 'train': '../SE/train/'}
output_folder = {'eval': '../SE/eval-asts/', 'train': '../SE/train-asts/'}
csv_name = {'eval': '../SE/eval', 'train': '../SE/train'}

table = {}
for key in directory_name:
    if not os.path.isdir(output_folder[key]):
        os.makedirs(output_folder[key])

    directory = os.fsencode(directory_name[key])
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): 
            splits = filename.split('_')
            if not splits[0] in table:
                table[splits[0]] = {}
                table[splits[0]]["label"] = filename
            else:
                table[splits[0]]["label"] = filename
        elif filename.endswith(".py"):
            splits = filename.split('.')
            if not splits[0] in table:
                table[splits[0]] = {}
                table[splits[0]]["input"] = filename
            else:
                table[splits[0]]["input"] = filename
            f = open(directory_name[key] + filename, 'r')
            tree = ast2json.ast2json(ast.parse(f.read()))
            out = open(output_folder[key] + splits[0] + '.json', 'w')
            table[splits[0]]['ast'] = splits[0] + '.json'
            out.write(json.dumps(tree))
            f.close()
    data = {'input': [], 'label': [], 'ast': []}

    for file_key in table:
        data['input'].append(table[file_key]['input'])
        data['label'].append(table[file_key]['label'])
        data['ast'].append(table[file_key]['ast'])

    pd.DataFrame(data).to_csv(csv_name[key] + '.csv', index=False)



