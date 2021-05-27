import os
import json

def parse (dataset_str):

    '''
    dataset_str : ['train', 'eval'], 
                    used for accessing ASTs and saving paths
    '''

    # Read contents of ASTs directory
    filenames = os.listdir('./SE/SE/'+ dataset_str +'-asts/') 
    
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

        # Read contents of AST file and parse nested JSON AST file
        json_li = json.loads(open('./SE/SE/'+ dataset_str +'-asts/'+filename).read())
        
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
        processed[filename]['file'] = './SE/SE/'+ dataset_str +'-asts/'+filename
        processed[filename]['paths'] = {}

        for k in path_names:
            processed[filename]['paths'][k] = []
            for i in path_names[k]:
                processed[filename]['paths'][k] += nodes[i]


    # print(processed)


    with open('./processed/'+dataset_str+'-processed.json', 'w') as fp:
        json.dump(processed, fp)

parse('train')
parse('eval')