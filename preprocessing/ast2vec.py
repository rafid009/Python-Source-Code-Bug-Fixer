from gensim import models
import torch

class Ast2Vec(object):
    def __init__(self, model_file) -> None:
        super().__init__()
        self.model = models.FastText.load(model_file)

    def get_tensor_representaion(self, ast):
        nodes_list = []
        for node in ast:
            nodes_list.append(self.model.wv[node])
        return torch.Tensor(nodes_list)



