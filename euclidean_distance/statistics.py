import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('../kien_vgg_face_cv2_euclidean_distance.csv')
print(df.shape)
# exit()
df = df.iloc[:, 1:]

array = df.to_numpy()
same_distance = array.diagonal()
# print(same_distance.shape)
array_without_diagonal = array.copy()
np.fill_diagonal(array_without_diagonal, np.inf)
diff_distance_0 = np.min(array_without_diagonal, axis=0)
# diff_distance_0 = np.min(array_without_diagonal, axis=1)
result = pd.DataFrame({"same" : same_distance, "diff" : diff_distance_0})
result.to_csv("kien.csv", index=False)

plt.hist(same_distance, bins=100)
plt.hist(diff_distance_0, bins=100, alpha=0.7, color='r')
plt.legend(['same person', 'diff person'])

plt.show()

