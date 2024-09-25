import torch.nn as nn
import numpy as np

class PositionalEncodings(nn.Module):
    def __init__(self, max_length, dim):
        self.max_length = max_length
        self.dim = dim
        self.positions = np.zeros((max_length, dim))
        self.positions[:, 0::2] = np.sin(np.arange(max_length).rehape(-1, 1) / (10000 ** np.arange(0, dim, 2) / dim))
        self.positions[:, 1::2] = np.cos(np.arange(max_length).rehape(-1, 1) / (10000 ** np.arange(1, dim, 2) / dim))

    def calculate(self, x):
        result = x + self.positions[:, :x.size(1), :]
        return result
        
                