import pandas as pd
import matplotlib.pyplot as plt


df_long = pd.read_csv(
    "200-600khz.csv",
    skiprows=1,          # skip "Trace2,"
    header=None,
    engine="python"
)
df_long_part2 = pd.read_csv(
    "10-100khz.csv",
    skiprows=1,          # skip "Trace2,"
    header=None,
    engine="python"
)
df45 = pd.read_csv(
    "10-100khz_short.csv",
    skiprows=1,          # skip "Trace2,"
    header=None,
    engine="python"
)

def clean_trace(df, freq_col=0, amp_col=2):
    """
    Cleans messy trace CSV format like:
    Freq, Hz, Amp, dBm
    and returns numeric DataFrame with columns:
    Freq_Hz, Amp_dBm
    """
    
    df_clean = df[[freq_col, amp_col]].copy()
    df_clean.columns = ["Freq_Hz", "Amp_dBm"]

    df_clean["Freq_Hz"] = pd.to_numeric(df_clean["Freq_Hz"], errors="coerce")
    df_clean["Amp_dBm"] = pd.to_numeric(df_clean["Amp_dBm"], errors="coerce")

    df_clean = df_clean.dropna().reset_index(drop=True)

    return df_clean


# tr_15khz = clean_trace(dftest)
# tr_30khz = clean_trace(df3)
tr_45khz = clean_trace(df45)

fig, ax = plt.subplots(3, 1, figsize=(10,7))

# ax[0].plot(tr_15khz["Freq_Hz"], tr_15khz["Amp_dBm"])
# ax[1].plot(tr_30khz["Freq_Hz"], tr_30khz["Amp_dBm"])
ax[2].plot(tr_45khz["Freq_Hz"], tr_45khz["Amp_dBm"])
ax[2].set_xlabel("Frequency (Hz)")
for i in range(3):
    ax[i].set_ylabel("Amplitude (dBm)")

plt.show()
