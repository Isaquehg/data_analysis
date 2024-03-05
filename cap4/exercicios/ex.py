import numpy as np

# 1)
print('-----------------------------------------------------')
array1 = np.linspace(0, 1, 21)
print(f'Array linearmente espacado de 0 a 1, com 21 elementos: {array1}')

# 2)
print('-----------------------------------------------------')
array_pares1 = np.arange(0, 51, 2)
array_pares2 = np.arange(50, 101, 2)
print(f'Array de 0 a 51: {array_pares1}')
print(f'Array de 100 a 50: {array_pares2[::-1]}')

array_pares_final = np.sort(np.concatenate([array_pares1, array_pares2[::-1]]))

print(f'Concatenacao ordenada entre arrays: {array_pares_final}')

# 3)
print('-----------------------------------------------------')
print(f'Ordem decrescente da questao 2:\n {np.flip(array_pares_final)}')

# 4)
print('-----------------------------------------------------')
array_ones = np.ones((3, 4))
print(f'Array de ones 3x4: \n {array_ones}')

print(f'Array 3x4 em 1-D: \n {np.reshape(array_ones, (1, 12))}')

# 5)
print('-----------------------------------------------------')
array2 = np.ones((5, 2))
print(f'Shape: {array2.shape}\n Dimensions: {array2.ndim}\n Size: {array2.size}')

print(f'Esta matriz poderia se tornar um vetor de {array2.size} elementos.')
