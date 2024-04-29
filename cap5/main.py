import numpy as np
import pandas as pd

# Pandas' focuses about saving heterogeneous data
# This may lead to less optimized process

# Series (1D)
dict_1d = {'a': 10, 'b': 20, 'c': 30}

s1 = pd.Series(dict_1d)

s2 = pd.Series(data=[20, 30, 40], index=['a', 'b', 'd'])

# Math Operations
print(s1 + s2) # Must have same keys to be able to sum. Case not, will lead to NaN values
print(s1.add(s2, fill_value=0)) # Filling NaN

# Accessing Elements
print(s1['b'])
print(s1[['b', 'c']]) # Accessing multiple elements
print(s1[1:])

# Conditionals
print(s1[s1 > s1.mean()])
print(s1[s1/2 == 10])

# DataFrames (2D+)
np.random.seed(10)
df1 = pd.DataFrame(index=['a', 'b', 'c', 'd'], columns=['x', 'y', 'z'], data=np.random.randint(1, 50, (4, 3)))
print(df1)

# Slicing loc & iloc
print(df1.loc[['b', 'c'], ['x', 'y', 'z']])
print(df1.iloc[1:3, :]) # Like NumPy

# Importing
countries_df = pd.read_csv('cap5/paises.csv', delimiter=';', encoding='utf-8')
print('-----------------------------------------------------------')
print(countries_df.head())
print('-----------------------------------------------------------')
print(countries_df.tail(2))
print('-----------------------------------------------------------')
print(countries_df.columns)
print('-----------------------------------------------------------')
print(countries_df['Country'])

