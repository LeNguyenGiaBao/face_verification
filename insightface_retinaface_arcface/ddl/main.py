import numpy as np 
from ddl import DDL

emb_a = np.load('../../emb/insightface_emb_a.npy')
emb_b = np.load('../../emb/insightface_emb_b.npy')

emb_neg = emb_a * np.expand_dims(emb_a, axis=1)

ddl = DDL()
a, b, c = ddl.forward(emb_neg, emb_a, emb_b)
print(a, b, c)