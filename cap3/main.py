# COLLECTIONS
# TUPLE
'''
- () format
- Not muttable collection
'''

'''
nomes = ('Larry', 'Darry', 'Merry', 'Garry')

print(nomes)
print(nomes[0]) # Slicing
print(nomes[:2])
print(nomes[1:3]) # Last index element is exclusive!
print(nomes[-3:-1])
'''

# LISTS
''''
- [] format
- Muttable collection
- All CRUD operations
'''

'''
nomes = ['larry', 'Darry', 'Merry', 'Garry']

nomes.append('Perry') # Create
nomes[0] = 'Larry' # Update
del nomes[4] # Delete by index without return
nomes.pop(4) # Delete by index with return
nomes.remove('Merry') # Delete by value
print(nomes) # Retrieve
'''

# SETS
''''
- {} format
- Non-repeating data
- Keine Ordinung
- Doesn't have update operation
- Related to Math
'''

'''
nomes = {'Larry', 'Darry', 'Terry', 'Garry'}

print(nomes)
nomes.add('Perry') # Create
nomes.add('Garry') # Won't be added
nomes.remove('Terry')
'''

# DICTIONARY
''''
- {} format
- Personalized Keys
- Key-Value pairs
- All CRUD operations
'''

pessoa = {
    'nome': 'Larry', 
    'idade': 42
}

pessoa2 = {
    'nome': 'Darry', 
    'idade': 31
}

# Inner collections
pessoas = [pessoa, pessoa2]
print(pessoas[0]['nome']) # Accessing inner values

pessoa['sexo'] = 'M' # Create
del pessoa['idade'] # Delete
pessoa['nome'] = 'Garry' # Update
