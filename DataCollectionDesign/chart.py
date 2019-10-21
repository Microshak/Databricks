
from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
odf = pd.read_csv('TimeSeries.csv', sep=',')
df = odf.copy()
df['time'] = pd.to_datetime(df['time'])
df.set_index('time')


def plot_df(df, x, y, title="", xlabel='time', ylabel='sample', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='blue')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    return plt
plt = plot_df(df, x=df['time'], y=df['sample'], title='Vibrometer')
#plt.show()

print(odf)

minuite = odf.copy()


#minuite['time'] = minuite['time'].to_string()
isit =  minuite['time'].str.contains('00.0000')
minuite =minuite[isit]
    
print(minuite)


minuite['time'] = pd.to_datetime(minuite['time'])
minuite.set_index('time')


plt.plot(minuite['time'], minuite['sample'], color='red')
plt.show()


