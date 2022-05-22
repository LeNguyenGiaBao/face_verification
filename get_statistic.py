import pandas as pd 
import numpy as np 

df = pd.read_csv('./same_diff_person.csv')
print(df.shape)
print(df.head())

ranges = np.arange(0, 1.4, 0.01)
df1 = df.groupby(pd.cut(df['same'], ranges)).count()
df2 = df.groupby(pd.cut(df['diff'], ranges)).count()
print(df1.head())
print(df2.head())

result = pd.concat([df1['same'], df2['diff']], axis=1)
result.to_csv('count_same_diff_person.csv')
result.to_excel('count_same_diff_person.xlsx')
# print(pd.cut(df['same'], ranges))
# print(pd.cut(df['diff'], ranges))
# print(df.groupby(pd.cut(df['same'], ranges), pd.cut(df['diff'], ranges)).count())