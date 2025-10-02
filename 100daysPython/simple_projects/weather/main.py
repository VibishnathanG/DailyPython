#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot()
plt.savefig('plot.png')
print("Plot saved as plot.png")

