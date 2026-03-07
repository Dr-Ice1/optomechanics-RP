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
df_204 = load_file("2_04.csv")
df_500 = load_file("5_00.csv")
df_132 = load_file("13_2.csv")

## SPLIT EACH TRACE
#################################
t204 = df_204["Second"]
vg204 = df_204["Volt"]
vp204 = df_204["Volt.1"]*8

t500 = df_500["Second"]
vg500 = df_500["Volt"]
vp500 = df_500["Volt.1"]*8

t132 = df_132["Second"]
vg132 = df_132["Volt"]
vp132 = df_132["Volt.1"]*8
################################

## PLOTTING
#############################################################################
fig, ax = plt.subplots(3, 1, sharex=True, figsize=(14,10))

ax[0].plot(t204, vg204, label='Generator')
ax[0].plot(t204, vp204, label='Piezo*8')

ax[1].plot(t500, vg500, label='Generator')
ax[1].plot(t500, vp500, label='Piezo*8')

ax[2].plot(t132, vg132, label='Generator')
ax[2].plot(t132, vp132, label='Piezo*8')

ax[0].set_title("2.04 Vpp")
ax[1].set_title("5.00 Vpp")
ax[2].set_title("13.2 Vpp")

ax[0].set_ylabel('Voltage (V)')
ax[0].legend()
ax[0].grid(True)

ax[1].set_ylabel('Voltage (V)')
ax[1].legend()
ax[1].grid(True)

ax[2].set_xlabel('Time (s)')
ax[2].set_ylabel('Voltage (V)')
ax[2].legend()
ax[2].grid(True)
#############################################################################

# plt.savefig("opdr-A1.png", dpi=530)

plt.show()
