import numpy as np

arr = np.loadtxt('p1/brands.csv', dtype=str, delimiter=';', encoding='utf-8')
print(f'Header: {arr[0, :]}\n')

'''
['\ufeffBrand' 'Founded By/How it was founded' 'Founded In' 'Country'
 'Key People' 'Genre/Industry' 'Website' 'Rank in 2022' 'Rank in 2021'
 'Brand Value ($M) in 2022' 'Brand Value ($M) in 2021' '% Change'
 'Rating in 2022' 'Rating in 2021']
'''

#Questão 1
#Mostre o quanto ($) a empresa Microsoft valorizou de 2021 para 2022
microsoft_filter = np.char.find(arr, 'Microsoft')>=0
microsoft_2021_value = arr[microsoft_filter[:, 0], 10]
microsoft_2022_value = arr[microsoft_filter[:, 0], 9]

growth = np.float64(microsoft_2022_value[0]) - np.float64(microsoft_2021_value[0]) # Usando index [0] para remover warning de conversao ndarray para float...
print(f'Valorização da Microsoft de 2021 para 2022[$M]: ${growth}\n')

#Questão 2
#Mostre o nome de todas as marcas que começam com a letra 'A'. Em seguida, ordene o resultado em ordem alfabética;
brands = arr[:, 0]
a_brands_filter = np.char.find(brands, 'A', start=0, end=1)>=0
a_brands_ordered = np.sort(brands[a_brands_filter])

print(f'Marcas que começam com A, em ordem alfabética: {a_brands_ordered}\n')

#Questão 3
#Mostre a porcentagem de empresas deste dataset que são dos Estados Unidos
countries = arr[:, 3]
n_companies = np.count_nonzero(countries[1:])
us_companies_filter = np.char.find(arr[:, 3], 'United States')>=0
n_us_companies = np.count_nonzero(brands[us_companies_filter])
ratio_us_companies = n_us_companies / n_companies
print(f'Porcentagem de empresas dos Estados Unidos: {ratio_us_companies*100}%\n')

#Questão 4
#Faça um Slicing no dataset e extraia apenas as colunas "nome da marca, por quem foi fundada e o ano que ela foi fundada". Em seguida, mostre apenas o nome das empresas fundadas depois dos anos 2000;
arr2 = arr[:, 0:3]

founded_after_2000s_filter = np.char.find(arr2[1:, 2], '20')>=0
brands_without_header = arr[1:, 0]
founded_after_2000s = brands_without_header[founded_after_2000s_filter]

print(f'Empresas fundadas depois de 2000: {founded_after_2000s}\n')

#Questão 5
#Busque os diferentes anos em que as empresas foram fundadas. Em seguida, mostre em qual ano mais empresas abriram as portas.
years_founded_unique, counts = np.unique(arr[1:, 2], return_counts=True)
more_business_year = np.argmax(counts)
more_new_business = years_founded_unique[more_business_year]

print(f'Ano que mais empresas foram abertas: {more_new_business}')


