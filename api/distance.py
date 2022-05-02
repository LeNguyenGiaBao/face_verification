import numpy as np 

def findEuclideanDistance(in_emb, out_emb):
    out_emb = np.expand_dims(out_emb,axis=1)
    euclidean_distance = in_emb - out_emb
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance), axis=2)
    euclidean_distance = np.sqrt(euclidean_distance)

    print(euclidean_distance)
    euclidean_distance = np.min(euclidean_distance)
    print(euclidean_distance)
    return euclidean_distance
