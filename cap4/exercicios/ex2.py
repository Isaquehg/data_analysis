import numpy as np

# 1)
np.random.seed(5)
arr1 = np.random.uniform(-1.0, 1.0, 10)
print(f"Random array numbers between -1 and 1:\n{arr1}")
arr1_multiplied = arr1 * 100

arr1_integers = np.floor(arr1_multiplied)
print(f"Integer part from array:\n{arr1_integers}")

# 2)
np.random.seed(10)
arr2 = np.random.randint(0, 51, (4, 4))
print(f"Array from 0 to 50, 4x4:\n{arr2}")

# 3)
total_mean = np.mean(arr2)
mean_x = np.mean(arr2, 0)
mean_y = np.mean(arr2, 1)
print(f"Total Mean: {total_mean}\nX axis: {mean_x}\nY axis: {mean_y}")
print(f"Greatest X mean: {mean_x.max()}\nGreatest Y mean: {mean_y.max()}")

# 4)
unique, counts = np.unique(arr2, return_counts=True)
count_dict = dict(zip(unique, counts))
arr4 = np.stack((unique, counts), axis=0)
print(f"Unique numbers and its repetitions:\n{arr4}")

print(f"Repeated numbers: {arr4[0, arr4[1]>1]}")
