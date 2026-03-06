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
vg204 = df_204["Volt"]/2
vp204 = df_204["Volt.1"]*6

t500 = df_500["Second"]
vg500 = df_500["Volt"]/3
vp500 = df_500["Volt.1"]*6

t132 = df_132["Second"]
vg132 = df_132["Volt"]/8
vp132 = df_132["Volt.1"]*8
################################

## PEAKS FOR 5.00 V
####################################################################
mask = (t500 > -0.0564) & (t500 < -0.0462)
vp_window = vp500[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.12, 0.2))
peaks_vp500_1 = np.where(mask)[0][peaks_local]

mask = (t500 > -0.046) & (t500 < -0.0392)
vp_window = vp500[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.12, 0.2))
peaks_vp500_2 = np.where(mask)[0][peaks_local]

mask = (t500 > -0.01664) & (t500 < -0.00849)
vp_window = vp500[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.12, 0.203))
peaks_vp500_3 = np.where(mask)[0][peaks_local]

mask = (t500 > -0.0062) & (t500 < 0.0014)
vp_window = vp500[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.15, 0.2))
peaks_vp500_4 = np.where(mask)[0][peaks_local]

mask = (t500 > 0.02358) & (t500 < 0.032)
vp_window = vp500[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.17, 0.2))
peaks_vp500_5 = np.where(mask)[0][peaks_local]

mask = (t500 > .034) & (t500 < .04144)
vp_window = vp500[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.166, 0.2))
peaks_vp500_6 = np.where(mask)[0][peaks_local]

peak_lists = [peaks_vp500_1, peaks_vp500_2, peaks_vp500_3, peaks_vp500_4, peaks_vp500_5, peaks_vp500_6]
plen500 = sum(len(p) for p in peak_lists)
####################################################################

## PEAKS FOR 13.2 V
####################################################################
mask = (t132 > -0.057) & (t132 < -.04857)
vp_window = vp132[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.13, 0.17))
peaks_vp132_1 = np.where(mask)[0][peaks_local]

mask = (t132 > -0.046) & (t132 < -.0358)
vp_window = vp132[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.13, 0.2))
peaks_vp132_2 = np.where(mask)[0][peaks_local]

mask = (t132 > -0.0168) & (t132 < -.0083)
vp_window = vp132[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.11, 0.2))
peaks_vp132_3 = np.where(mask)[0][peaks_local]

mask = (t132 > -.0066) & (t132 < .0045)
vp_window = vp132[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.1, 0.2))
peaks_vp132_4 = np.where(mask)[0][peaks_local]

mask = (t132 > .0235) & (t132 < .0317)
vp_window = vp132[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.1, 0.2))
peaks_vp132_5 = np.where(mask)[0][peaks_local]

mask = (t132 > .0335) & (t132 < .044)
vp_window = vp132[mask]
peaks_local, properties = find_peaks(vp_window, height=(0.1, 0.2))
peaks_vp132_6 = np.where(mask)[0][peaks_local]

peak_lists = [peaks_vp132_1, peaks_vp132_2, peaks_vp132_3, peaks_vp132_4, peaks_vp132_5, peaks_vp132_6]
plen132 = sum(len(p) for p in peak_lists)
####################################################################

## CALCULATING THE RESPONSIVITY
####################################################################
l = 635e-9  # wavelength (m)

def resp_from_peak_group(vg, peaks_idx, f, wavelength=l, use_intervals=False, abs_dV=True):
    """
    vg: pandas Series (your already-scaled generator voltage trace, e.g. vg500)
    peaks_idx: array of ORIGINAL indices (e.g. peaks_vp500_1)
    use_intervals:
        True  -> p = len(peaks)-1  (fringes between successive peaks)  [recommended]
        False -> p = len(peaks)    (if your lab defines it that way)
    abs_dV: take absolute value of dV
    """
    peaks_idx = np.asarray(peaks_idx, dtype=int)
    if peaks_idx.size < 2:
        return np.nan, np.nan, np.nan, 0  # not enough peaks for dV / fringes

    peaks_idx.sort()
    i0, i1 = peaks_idx[0], peaks_idx[-1]

    V_first = float(vg.iloc[i0])
    V_last  = float(vg.iloc[i1])
    dV = f*(V_last - V_first)
    if abs_dV:
        dV = abs(dV)

    p = (peaks_idx.size - 1) if use_intervals else peaks_idx.size

    R = (p * wavelength) / (2 * dV) if dV != 0 else np.inf
    return R, dV, V_first, V_last, p, i0, i1

groups500 = [peaks_vp500_1, peaks_vp500_2, peaks_vp500_3, peaks_vp500_4, peaks_vp500_5, peaks_vp500_6]

for k, g in enumerate(groups500, 1):
    R, dV, V0, V1, p, i0, i1 = resp_from_peak_group(vg500, g, f=3)
    print(f"5.00V group{k}: p={p:2d}, V0={V0:+.4f}, V1={V1:+.4f}, dV={dV:.4f}, R={R:.3e} m/V")

groups132 = [peaks_vp132_1, peaks_vp132_2, peaks_vp132_3, peaks_vp132_4, peaks_vp132_5, peaks_vp132_6]

for k, g in enumerate(groups132, 1):
    R, dV, V0, V1, p, i0, i1 = resp_from_peak_group(vg132, g, f=8)
    print(f"13.2V group{k}: p={p:2d}, V0={V0:+.4f}, V1={V1:+.4f}, dV={dV:.4f}, R={R:.3e} m/V")
####################################################################

## MEAN AND STUFF OF RESPONSIVITY
####################################################################
R_values_500 = []
R_values_132 = []

# 5.00 V
for g in groups500:
    R, dV, V0, V1, p, i0, i1 = resp_from_peak_group(vg500, g, 3)
    R_values_500.append(R)

# 13.2 V
for g in groups132:
    R, dV, V0, V1, p, i0, i1 = resp_from_peak_group(vg132, g, 8)
    R_values_132.append(R)

def statistical_analysis(R_values):
    R_array = np.array(R_values)

    mean_R = np.mean(R_array)
    std_R = np.std(R_array, ddof=1)          # sample standard deviation
    sem_R = std_R / np.sqrt(len(R_array))    # standard error of mean

    return mean_R, std_R, sem_R

mean500, std500, err500 = statistical_analysis(R_values_500)
mean132, std132, err132 = statistical_analysis(R_values_132)

print("\n--- Statistical Analysis ---")
print(f"Responsivity (5.00 Vpp):")
print(f"Mean = {mean500:.3e} m/V")
print(f"Std  = {std500:.3e} m/V")
print(f"Error (SEM) = {err500:.3e} m/V")

print("\nResponsivity (13.2 Vpp):")
print(f"Mean = {mean132:.3e} m/V")
print(f"Std  = {std132:.3e} m/V")
print(f"Error (SEM) = {err132:.3e} m/V")
####################################################################

## PLOTTING
#############################################################################
fig, ax = plt.subplots(3, 1, sharex=True, figsize=(14,10))

ax[0].plot(t204, vg204, label='Generator/2')
ax[0].plot(t204, vp204, label='Piezo*6')

ax[1].plot(t500, vg500, label='Generator/3')
ax[1].plot(t500, vp500, label='Piezo*6')
ax[1].plot(t500[peaks_vp500_1], vp500[peaks_vp500_1], 'x')
ax[1].plot(t500[peaks_vp500_2], vp500[peaks_vp500_2], 'x')
ax[1].plot(t500[peaks_vp500_3], vp500[peaks_vp500_3], 'x')
ax[1].plot(t500[peaks_vp500_4], vp500[peaks_vp500_4], 'x')
ax[1].plot(t500[peaks_vp500_5], vp500[peaks_vp500_5], 'x')
ax[1].plot(t500[peaks_vp500_6], vp500[peaks_vp500_6], 'x')
print("Total peaks 5.00 V:", plen500)

ax[2].plot(t132, vg132, label='Generator/8')
ax[2].plot(t132, vp132, label='Piezo*8')
ax[2].plot(t132[peaks_vp132_1], vp132[peaks_vp132_1], 'x')
ax[2].plot(t132[peaks_vp132_2], vp132[peaks_vp132_2], 'x')
ax[2].plot(t132[peaks_vp132_3], vp132[peaks_vp132_3], 'x')
ax[2].plot(t132[peaks_vp132_4], vp132[peaks_vp132_4], 'x')
ax[2].plot(t132[peaks_vp132_5], vp132[peaks_vp132_5], 'x')
ax[2].plot(t132[peaks_vp132_6], vp132[peaks_vp132_6], 'x')
print("Total peaks 13.2 V:", plen132)

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

## CALCULATING THE FINAL ANSWER
#############################################################################
sem500 = err500
sem132 = err132

def sci_pm(mean, err, sig_err=2):
    exp = int(np.floor(np.log10(abs(mean))))
    m = mean / (10**exp)
    e = err  / (10**exp)

    err_exp = int(np.floor(np.log10(abs(e))))
    decimals = max(sig_err - 1 - err_exp, 0)

    e_rounded = round(e, decimals)
    m_rounded = round(m, decimals)

    return f"({m_rounded:.{decimals}f} ± {e_rounded:.{decimals}f}) × 10^{exp}"

# Final formatted results
print("--- Final results (mean ± SEM) ---")
print(f"5.00 Vpp:  R = {sci_pm(mean500, sem500)} m/V")
print(f"13.2 Vpp:  R = {sci_pm(mean132, sem132)} m/V")

# Consistency check
diff = abs(mean500 - mean132)
combined = np.sqrt(sem500**2 + sem132**2)
z = diff / combined

print("\n--- Consistency check ---")
print(f"|Δ| = {diff:.3e} m/V")
print(f"σ_combined = {combined:.3e} m/V")
print(f"z = {z:.2f}  (z<1 => consistent within 1σ)")
#############################################################################


plt.show()
