import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(18, 8))

# Exercise 1
print('---------------------------------------------------------------')
space_df = pd.read_csv('cap6/exercises/space.csv', delimiter=';')

usa_missions_cond = space_df['Location'].str.contains('USA', na=False)
usa_missions = space_df[usa_missions_cond]

n_space_companies_usa = usa_missions['Company Name'].unique().size
print(f'Number USA Space Companies: {n_space_companies_usa}')

china_missions_cond = space_df['Location'].str.contains('China', na=False)
china_missions = space_df[china_missions_cond]

n_space_companies_china = china_missions['Company Name'].unique().size
print(f'Number China Space Companies: {n_space_companies_china}')
print('---------------------------------------------------------------')

# First Subplot
plt.subplot(1, 3, 1)
plt.title('Number of Space Companies in USA and China')
plt.xlabel('Country')
plt.ylabel('Number of Space Companies')
plt.bar(['USA', 'China'], [n_space_companies_usa, n_space_companies_china], color='blue')

# Exercise 2
countries_df = pd.read_csv('cap6/exercises/paises.csv', delimiter=';')

northern_countries_cond = countries_df['Region'].str.contains('NORTHERN AMERICA', na=False)
northern_countries = countries_df[northern_countries_cond]

# Second Subplot
plt.subplot(1, 3, 2)
plt.title('Birthrate in Northern America')
plt.xlabel('Country')
plt.ylabel('Birthrate')
plt.plot(northern_countries['Country'], northern_countries['Birthrate'], '.-b', linewidth=3, markersize=15)

# Thrid Subplot
plt.subplot(1, 3, 3)
plt.title('Deathrate in Northern America')
plt.xlabel('Country')
plt.ylabel('Deathrate')
plt.plot(northern_countries['Country'], northern_countries['Deathrate'], '.-r', linewidth=3, markersize=15)


plt.tight_layout() # Correct chart to fit better inside figure size
plt.show()









