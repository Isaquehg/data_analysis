import pandas as pd
import numpy as np

df = pd.read_csv('cap5/paises.csv', delimiter=';')

# 1)
print('----------------------------------------------------------------')
countries_df = pd.read_csv('cap5/paises.csv', delimiter=';', encoding='utf-8')
regions_df = countries_df['Region']
oceania_countries = countries_df[regions_df.str.contains('OCEANIA')]
n_oceania_countries = oceania_countries['Country'].count()
print(f'Oceania countries: \n{oceania_countries}')
print(f'There are {n_oceania_countries} Countries in Oceania')
print('----------------------------------------------------------------')

# 2) Literacy (%)
literacy_df = countries_df['Literacy (%)']
print(f'Literacy Mean Worldwide: {literacy_df.mean(axis=0)}%')
print('----------------------------------------------------------------')

# 3)
countries = countries_df['Country']
population_df = countries_df['Population']
greatest_pop_index = population_df.argmax(axis=0)
greatest_pop = population_df.max()
greatest_pop_country = countries[greatest_pop_index]
greatest_pop_region = regions_df[greatest_pop_index]

print(f'World Greatest Population is {greatest_pop_country}, located in {greatest_pop_region}')
print('----------------------------------------------------------------')

# 4)
coastline_areas = countries_df['Coastline (coast/area ratio)']
no_coastline_indexes = (coastline_areas[coastline_areas == 0]).keys()
no_coastline_countries = countries[no_coastline_indexes]
print(f'Countries without Coastline: \n{no_coastline_countries}')
no_coastline_countries.to_csv('./cap5/exercises/noCoast.csv')
