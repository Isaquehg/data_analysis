import numpy as np

# ONLY SAME DATA TYPES IN NDARRAY!

array1 = np.array([1, 2, 3, 4]) # 1-D Numpy Array
print(type(array1))

array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) # 2-D Numpy Array
print(array2)

# Random data feeding
rd_array = np.ones(9)
print(rd_array)

rd_array2 = np.zeros((2, 2))
print(rd_array2)

# Arange Array
rd_array3 = np.arange(9)
print(rd_array3)

rd_array4 = np.arange(128, 256, 2) # Start, stop, step
print(rd_array4)

# Reshape array
rd_array = rd_array.reshape(3, 3)
print(rd_array)

rd_array = rd_array.reshape(9, 1) # Convert to alternative shape (Shape must be compatible)
print(rd_array)

# Sort
array1 = np.sort(array1)
array1 = np.flip(np.sort(array1)) # Descending order

# OPERATIONS AMONG ARRAYS (Index by index)
# Summing arrays
array1 = np.arange(10, 20, 1)
array2 = np.arange(30, 40, 1)
print(array1 + array2)

# Concatenate
print(np.concatenate([array1, array2], axis=0))

# ARRAY PROPERTIES
print(array1.size)
print(array1.ndim)
print(array1.shape)
