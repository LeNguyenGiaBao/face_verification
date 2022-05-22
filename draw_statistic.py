import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

# data = open('./sim_same_person.txt', 'r').readlines()
# data = [i.replace]

df = pd.read_csv('./sim_same_person.txt', sep='\n', header=None)
print(df.head())
print(df[0])
# df = pd.read_csv('./sim_same_person_cosine.txt', sep='\n', header=None)
df2 = pd.read_csv('./sim_different_person.csv')
# print(df2.head())
# print(df2.max())
# print(df2.nlargest(2))

largest = pd.DataFrame(np.sort(df2.values)[:,-3:], columns=['3rd-largest', '2nd-largest','largest'])
# print(largest.shape)
# print(largest.head())
# print(largest['3rd-largest'].to_numpy())

df_same_diff_person = pd.concat([df[0], largest['3rd-largest']], axis=1)
df_same_diff_person.to_csv('same_diff_person.csv')

# ax = df.plot.hist(bins=100, alpha=0.5)
plt.hist(df, bins=100)
plt.hist(largest['3rd-largest'], bins=100, alpha=0.7, color='r')
plt.legend(['same person', 'diff person'])

plt.show()