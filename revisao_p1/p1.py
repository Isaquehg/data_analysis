import numpy as np

arr = np.loadtxt('revisao_p1/paises.csv', dtype=str, delimiter=';', encoding='utf-8')

print(f'\nCSV properties:\nShape: {arr.shape}\nNdim: {arr.ndim}\nSize: {arr.size}\nHeader: {arr[0,:]}\n')

# 1) Country, Region, Population e Area
arr_new = arr[:, 0:4]
print(f"New Header: {arr_new[0, :]}\n")

# 2) Unique Regions
regions = arr_new[:, 1]
unique_regions = np.unique(arr_new)
print(f"Diferent Regions: {unique_regions}\n")

# 3) Literacy (%)
literacy = np.float64(arr[1:, 9])
literacy_mean = np.mean(literacy)
print(f"Literacy Mean: {literacy_mean}\n")

# 4) Northern Countries
regions = arr_new[1:, 1]
filter_northern = np.char.find(regions, 'NORTHERN AMERICA')>=0

northern_america_countries = np.count_nonzero(regions[filter_northern])
print(f"Northern America Countries: {northern_america_countries}\n")

# 5) Greatest GDP Latan & Carib
filter_latin_carib = arr[np.char.find(arr[:, 1], 'LATIN AMER. & CARIB')>=0]

filter_gdp_index = np.argmax(np.float64(filter_latin_carib[:, 8]))

print(f"Greatest Latin America & Carib GDP: {filter_latin_carib[filter_gdp_index, 0]}")

