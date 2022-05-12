import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

emb_A = np.load('./emb/insightface_emb_a_norm.npy')
emb_B = np.load('./emb/insightface_emb_b_norm.npy')
# emb_A_norm = np.load('./emb/insightface_emb_a_norm.npy')
# emb_B_norm = np.load('./emb/insightface_emb_b_norm.npy')

norm_emb_A = np.linalg.norm(emb_A, axis=1)
norm_emb_B = np.linalg.norm(emb_B, axis=1)


mul = np.dot(emb_A, emb_B.T)

norm_emb_A = norm_emb_A.reshape(1671, 1)
norm_emb_B = norm_emb_B.reshape(1, 1671)

mul_norm = np.dot(norm_emb_A, norm_emb_B)

cosine = mul / mul_norm
cosine_distance = 1 - cosine
df = pd.DataFrame(cosine_distance)
# print(df.head())
df.to_csv('./statistics_csv/insightface_norm_cosine_distance.csv', header=None, index=None)

same_distance = np.diagonal(cosine_distance)
print(same_distance)
cosine_distance_copy = cosine_distance.copy()
np.fill_diagonal(cosine_distance_copy, np.inf)
diff_distance = np.min(cosine_distance_copy, axis=1)

plt.hist(same_distance, bins=100)
plt.hist(diff_distance, bins=100, alpha=0.7, color='r')
plt.legend(['same person', 'diff person'])
plt.savefig('./statistics_chart/insightface_norm_cosine_distance.png')

plt.show()