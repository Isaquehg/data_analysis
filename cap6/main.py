import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = np.array([1, 2, 3, 4])
y1 = x1*2 # Broadcasting

y2 = x1**2

# COMPOSED CHART
'''plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.plot(x1, y1, 's:m', # Marker - Line - Colour
         x1, y2, '*:b', # Marker - Line - Colour
         linewidth=5, markersize=20) # Universal
plt.show()'''

# SUBPLOTTING
plt.subplot(1, 2, 1) #NRows, NCols, Index
plt.title('Linear')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.plot(x1, y1, 'x--r')

plt.subplot(1, 2, 2)
plt.title('Exponencial')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.plot(x1, y2, '*--b')

plt.show()
