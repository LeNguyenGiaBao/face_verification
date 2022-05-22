import pandas as pd 
import matplotlib.pyplot as plt
from pyparsing import col 

same = pd.read_csv('./data/ninh_vao_ra_cosine.csv')
diff = pd.read_csv('./data/ninh_vao_thay_ra_cosine.csv')

plt.hist(same.iloc[:, 2])
plt.hist(diff.iloc[:, 2], alpha=0.7, color='r')

plt.show()