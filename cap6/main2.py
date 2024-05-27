import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('cap6/paises.csv', delimiter=';')

# Biggest countries
largest = countries_df.nlargest(6, 'Area (sq. mi.)')

# SCATTER CHART
plt.scatter(largest['Country'], largest['Area (sq. mi.)'],  largest['GDP ($ per capita)']/50)
plt.xlabel('Country')
plt.ylabel('Area (sq. mi.)')
plt.show()

# BAR CHART

# PIE CHART

