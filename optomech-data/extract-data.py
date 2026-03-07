## IMPORT LIBS
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

## DEFINE FUNCTION for loading in traces
def load_file(name):
    df = pd.read_csv(name, sep=",", header=1, skipinitialspace=True, index_col=False, engine="python")
    return df

## MAKE DATAFRAME FROM TRACES 
df = load_file("abz.csv")

t = df["Second"]
vg = df["Volt"]
vp = df["Volt.1"]

fig, ax = plt.subplots(3, 1, sharex=True, figsize=(14,10))

ax[0].plot(t, vg, label='Generator')
ax[1].plot(t, vp, label='Piezo')

plt.show()


