import torch.nn as nn
import torch.nn.functional as F

class MultiheadAttention(nn.Module):
    def __init__(self, dim, heads):
        super(MultiheadAttention).__init__()
        assert dim % heads == 0

        #head dimensions
        self.dim = dim
        self.heads = heads 
        self.heads_dim = dim // heads

        #initializing matrices
        self.q = nn.Linear(dim, dim)
        self.k = nn.Linear(dim, dim)
        self.v = nn.Linear(dim, dim)

        #
        self.out = nn.Linear(dim, dim)

    def forward(self, query, key, values):
        batch_size = query.size(0)
        
        q_u = self.q(query)
        k_u = self.k(key)
        v_u = self.v(values)

        
        


    def scaled_dot_product_attention(self, query, key, value):
        d_k = query.size(-1)

        scores = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))

        attention_weights = F.softmax(scores, dim=-1)

        output = torch.matmul(attention_weights, value)
        
        return output, attention_weights

        
