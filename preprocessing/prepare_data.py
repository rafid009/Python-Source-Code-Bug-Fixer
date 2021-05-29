import os
import sys
from typing import Type
import pandas as pd
import numpy as np
import ast #import parse
import json

directory_name = {'eval': './data/eval/', 'train': './data/train/'}
output_folder = {'eval': './data/eval-asts/', 'train': './data/train-asts/'}
processed_path_slices = './processed/'
csv_name = {'eval': './data/eval', 'train': './data/train'}


def read_file_to_string(filename):
    f = open(filename, 'rt')
    s = f.read()
    f.close()
    return s

def process_paths(dataset_folder, dataset_str):

    '''
    dataset_str : ['train', 'eval'], 
                    used for accessing ASTs and saving paths
    '''
    print(dataset_folder)
    # Read contents of ASTs directory
    filenames = os.listdir(dataset_folder) 
    
    # Filter out non JSON files
    filenames = [filename for filename in filenames if filename.endswith('.json')]
    # Sort list of filenames
    filenames.sort()

    # Create dictionary for storing processed data
    processed = {}

    # path names
    path_names = {
        '0':[0],
        '0-1' :[0,1],
        '0-2' :[0,2],
        '0-1-3' :[0,1,3],
        '0-1-4' : [0,1,4],
        '0-2-3' :[0,2,3],
        '0-2-4' : [0,2,4],
        '0-1-3-5' :[0,1,3,5],
        '0-1-4-5' : [0,1,4,5],
        '0-2-3-5' :[0,2,3,5],
        '0-2-4-5' : [0,2,4,5],     
    }

    for filename in filenames:
        print(filename)
        # Read contents of AST file and parse nested JSON AST file
        json_li = json.loads(open(dataset_folder+filename).read())
        
        # Extract JSON objects representing conditional statements 
        #   i.e. where obj['type'] is either 'If' or 'orelse'
        conditionals = [(idx, obj) for idx, obj in enumerate(json_li) if (obj['type']=='If' or obj['type']=='orelse')]
        # bodies = [(idx, obj) for idx, obj in enumerate(json_li) if obj['type']=='body']

        leaves = []
        for idx in range(len(json_li)):
            if (json_li[idx]['type']=='NameLoad' 
                and json_li[idx]['value']=='paths' 
                and json_li[idx+1]['type']=='attr' 
                and json_li[idx+1]['value']=='append'):
                
                leaves.append((idx+2, json_li[idx+2]))
        
        nodes = []
 
        nodes.append(list(range(conditionals[0][0]))) # 0 -before 1st if statement, header code, root node
        nodes.append(list(range(conditionals[0][0],conditionals[1][0]))) # 1- first if
        nodes.append(list(range(conditionals[1][0],conditionals[2][0]))) # 2- first else
        nodes.append(list(range(conditionals[2][0],conditionals[3][0]))) # 3- second if
        nodes.append(list(range(conditionals[3][0],conditionals[4][0]))) # 4- second else
        nodes.append(list(range(conditionals[4][0],len(json_li)))) # 5-last stray if and footer code

        processed[filename] = {}
        processed[filename]['file'] = dataset_folder+filename
        processed[filename]['paths'] = {}

        for k in path_names:
            processed[filename]['paths'][k] = []
            for i in path_names[k]:
                processed[filename]['paths'][k] += nodes[i]
    if not os.path.isdir(processed_path_slices):
        os.makedirs(processed_path_slices)

    with open(processed_path_slices+dataset_str+'-processed.json', 'w') as fp:
        json.dump(processed, fp)
        
def parse_file(filename):
    global c, d
    tree = ast.parse(read_file_to_string(filename), filename)
    
    json_tree = []
    def gen_identifier(identifier, node_type = 'identifier'):
        pos = len(json_tree)
        json_node = {}
        json_tree.append(json_node)
        json_node['type'] = node_type
        json_node['value'] = identifier
        return pos
    
    def traverse_list(l, node_type = 'list'):
        pos = len(json_tree)
        json_node = {}
        json_tree.append(json_node)
        json_node['type'] = node_type
        children = []
        for item in l:
            children.append(traverse(item))
        if (len(children) != 0):
            json_node['children'] = children
        return pos
        
    def traverse(node):
        pos = len(json_tree)
        json_node = {}
        json_tree.append(json_node)
        json_node['type'] = type(node).__name__
        children = []
        if isinstance(node, ast.Name):
            json_node['value'] = node.id
        elif isinstance(node, ast.Num):
            json_node['value'] = str(node.n)
        elif isinstance(node, ast.Str):
            json_node['value'] = str(node.s)
        elif isinstance(node, ast.alias):
            json_node['value'] = str(node.name)
            if node.asname:
                children.append(gen_identifier(node.asname))
        elif isinstance(node, ast.FunctionDef):
            json_node['value'] = str(node.name)
        elif isinstance(node, ast.ClassDef):
            json_node['value'] = str(node.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                json_node['value'] = str(node.module)
        elif isinstance(node, ast.Global):
            for n in node.names:
                children.append(gen_identifier(n))
        elif isinstance(node, ast.keyword):
            json_node['value'] = str(node.arg)
        

        # Process children.
        if isinstance(node, ast.For):
            children.append(traverse(node.target))
            children.append(traverse(node.iter))
            children.append(traverse_list(node.body, 'body'))
            if node.orelse:
                children.append(traverse_list(node.orelse, 'orelse'))
        elif isinstance(node, ast.If) or isinstance(node, ast.While):
            children.append(traverse(node.test))
            children.append(traverse_list(node.body, 'body'))
            if node.orelse:
                children.append(traverse_list(node.orelse, 'orelse'))
        elif isinstance(node, ast.Try):
            children.append(traverse_list(node.body, 'body'))
            children.append(traverse_list(node.handlers, 'handlers'))
            if node.orelse:
                children.append(traverse_list(node.orelse, 'orelse'))
        elif isinstance(node, ast.arguments):
            children.append(traverse_list(node.args, 'args'))
            children.append(traverse_list(node.defaults, 'defaults'))
            if node.vararg:
                children.append(gen_identifier(node.vararg, 'vararg'))
            if node.kwarg:
                children.append(gen_identifier(node.kwarg, 'kwarg'))
        elif isinstance(node, ast.ExceptHandler):
            if node.type:
                children.append(traverse_list([node.type], 'type'))
            if node.name:
                children.append(traverse_list([node.name], 'name'))
            children.append(traverse_list(node.body, 'body'))
        elif isinstance(node, ast.ClassDef):
            children.append(traverse_list(node.bases, 'bases'))
            children.append(traverse_list(node.body, 'body'))
            children.append(traverse_list(node.decorator_list, 'decorator_list'))
        elif isinstance(node, ast.FunctionDef):
            children.append(traverse(node.args))
            children.append(traverse_list(node.body, 'body'))
            children.append(traverse_list(node.decorator_list, 'decorator_list'))
        else:
            # Default handling: iterate over children.
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.expr_context) or isinstance(child, ast.operator) or isinstance(child, ast.boolop) or isinstance(child, ast.unaryop) or isinstance(child, ast.cmpop):
                    # Directly include expr_context, and operators into the type instead of creating a child.
                    json_node['type'] = json_node['type'] + type(child).__name__
                else:
                    children.append(traverse(child))
                
        if isinstance(node, ast.Attribute):
            children.append(gen_identifier(node.attr, 'attr'))
                
        if (len(children) != 0):
            json_node['children'] = children
        return pos
    
    traverse(tree)
    return json.dumps(json_tree, separators=(',', ':'), ensure_ascii=False)

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
            # f = open(directory_name[key] + filename, 'r')
            # tree = ast2json.ast2json(ast.parse(f.read()))
            out = open(output_folder[key] + splits[0] + '.json', 'w')
            table[splits[0]]['ast'] = splits[0] + '.json'
            out.write(parse_file(directory_name[key] + filename))
            out.close()
            # f.close()
    data = {'input': [], 'label': [], 'ast': []}

    for file_key in table:
        data['input'].append(table[file_key]['input'])
        data['label'].append(table[file_key]['label'])
        data['ast'].append(table[file_key]['ast'])

    pd.DataFrame(data).to_csv(csv_name[key] + '.csv', index=False)
    process_paths(output_folder[key], key)



