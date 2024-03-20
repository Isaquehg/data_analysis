import numpy as np

arr = np.loadtxt('cap4/exercicios/space.csv', dtype=str, delimiter=';', encoding='utf-8')

print(f'\nCSV properties:\nShape: {arr.shape}\nNdim: {arr.ndim}\nSize: {arr.size}\nHeader: {arr[0,:]}\n')

# 1)
total_missions = arr[:,1]
total_missions = total_missions.size - 1  # Remove header

arr_headerless = arr[1:, :]
successes = (arr_headerless[arr_headerless[:, 7] == 'Success'][:,0]).size
success_ratio = successes / total_missions

print(f'Success Missions Ratio: {success_ratio * 100}%\n')

# 2)
# "Floating costs column"
arr_costs_float = np.array(arr_headerless[:, 6], dtype=np.float64)
total_costs = (arr_costs_float[arr_costs_float[:] > 0][:]).sum(axis=0)
print(f'Total Mission Costs [Millions USD]: ${total_costs}\n')

# 3)
arr_locations = arr_headerless[:, 2]
usa_missions = (arr_headerless[np.char.endswith(arr_locations, 'USA')][:, 0]).size
print(f'Number of USA Missions: {usa_missions}\n')

# 4)
spacex_missions_cost = np.float64(arr_headerless[arr_headerless[:, 1] == 'SpaceX'][:, 6])
spacex_most_expensive = spacex_missions_cost.max()

print(f'Most Expensive SpaceX Mission: ${spacex_most_expensive} millions USD\n')

# 5)
unique_companies, company_counts = np.unique(arr_headerless[:, 1], return_counts=True)

companies_missions = dict(zip(unique_companies, company_counts))

print("Missions by each Company:")
for company, mission_count in companies_missions.items():
  print(f"{company}: {mission_count} missions")
