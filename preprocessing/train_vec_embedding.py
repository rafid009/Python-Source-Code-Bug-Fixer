from gensim import models
import os
import json

ast_folders = ['./data/train-asts/', './data/eval-asts/', '../../py150/']

corpus = []
def to_string_list(code_list):
    return [str(c) for c in code_list]

def data_to_json(filename):
    i = 1
    f = open(filename, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        line = eval(line.strip())
        corpus.append(to_string_list(line))

    
for folder in ast_folders:
    directory = os.fsencode(folder)
    for file in os.listdir(directory):
        ast_file = os.fsdecode(file)
        if not ast_file.endswith(".json") or os.path.isdir(folder + ast_file):
            continue
        data_to_json(folder + ast_file)


code2vec = models.FastText(corpus, vector_size=128, window=5, min_count=5, workers=4,sg=1)
code2vec.save('code2vec.model')

# code2vec = models.FastText.load('code2vec.model')
# print("loaded")
# print(code2vec.wv.most_similar('{"type":"NameStore","value":"x"}', topn=10))
# print(type(code2vec.wv['{"type":"NameStore","value":"x"}']))
# data_to_json('../py150/python100k_train.json')