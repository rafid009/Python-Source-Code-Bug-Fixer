from gensim import models
import os

# ast_folders = ['../SE/train-asts/', '../SE/eval-asts/', '../corpus/']

# corpus = []

# for folder in ast_folders:
#     directory = os.fsencode(folder)
#     for file in os.listdir(directory):
#         ast_file = os.fsdecode(file)
#         if os.path.isdir(folder + ast_file):
#             continue
#         f = open(folder + ast_file, 'r')
#         splits = f.read().split()
#         corpus.append(splits)
#         f.close()

# code2vec = models.FastText(corpus, vector_size=128, window=5, min_count=5, workers=4,sg=1)
# code2vec.save('code2vec.model')

code2vec = models.FastText.load('code2vec.model')
print(code2vec.wv.most_similar('elif', topn=10))