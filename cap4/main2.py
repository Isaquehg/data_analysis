import numpy as np

# RANDOM NUMBERS
np.random.seed(10) # Seeding (Generate the same values even in different machines)
arr = np.random.randint(10, 20, 5)
print(arr)

# ORDER AN ARRAY of unique values (Set doesn't order it)
arr_unique = np.random.randint(0, 10, 15)
print(arr_unique)

print(set(arr_unique))

arr_unique = np.unique(arr_unique) # Unique is faster than set.
print(arr_unique)

# MATRICES
np.random.seed(10)
m1 = np.random.randint(1, 11, (3, 3))
#m1 = np.random.randint(1, 11, 9).reshape(3, 3)
print(m1)
print(m1.sum(axis=0)) # -> Axis=0: Vertical
print(m1.mean(axis=0)[0])

# BROADCASTING (Number X Array)
arr_broadcasting = np.random.randint(1, 11, 11)
print(arr_broadcasting * 10)
print(arr_broadcasting / 10)

# CONDITIONS (Filtering matrices values from specified conditions)
np.random.seed(10)
arr_condition = np.random.randint(1, 11, (3, 3))
arr_even = arr_condition[arr_condition%2==0] # Firstly, we create a "mask" condition then apply this mask as an index to the array slicing
print(arr_even)

arr_grt = arr_condition[arr_condition>arr_condition.mean()]
print(arr_grt)

# STRINGS
arr_string = np.array(['Giovani', 'Isaque', 'Luiza', 'Raissa'])

cond = np.char.find(arr_string, 's')>=0
print(arr_string[cond])




