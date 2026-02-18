# optomechanics-RP

![peaks](https://raw.githubusercontent.com/Dr-Ice1/optomechanics-RP/main/resources/resp-with-peaks.png)
![no-peaks](https://raw.githubusercontent.com/Dr-Ice1/optomechanics-RP/main/resources/responsivity.png)


--- Statistical Analysis ---
Responsivity (5.00 Vpp):
Mean = 1.233e-06 m/V
Std  = 2.648e-07 m/V
Error (SEM) = 1.081e-07 m/V

Responsivity (13.2 Vpp):
Mean = 1.179e-06 m/V
Std  = 2.604e-07 m/V
Error (SEM) = 1.063e-07 m/V



With p being number of peaks, V0 the voltage at the first peak of a group and V1 the last, dV the absolute difference between these two including the accounting factor of the data change, and finally R as the responsivity.

5.00V group1: p= 6, V0=+0.4267, V1=+0.8533, dV=1.2800, R=1.488e-06 m/V
5.00V group2: p= 5, V0=+0.4800, V1=-0.0267, dV=1.5200, R=1.044e-06 m/V
5.00V group3: p= 6, V0=+0.4400, V1=+0.8667, dV=1.2800, R=1.488e-06 m/V
5.00V group4: p= 5, V0=+0.4933, V1=-0.0533, dV=1.6400, R=9.680e-07 m/V
5.00V group5: p= 6, V0=+0.4533, V1=+0.8933, dV=1.3200, R=1.443e-06 m/V
5.00V group6: p= 5, V0=+0.4933, V1=-0.0533, dV=1.6400, R=9.680e-07 m/V
13.2V group1: p=17, V0=+0.3300, V1=+0.8200, dV=3.9200, R=1.377e-06 m/V
13.2V group2: p=17, V0=+0.4400, V1=-0.2200, dV=5.2800, R=1.022e-06 m/V
13.2V group3: p=18, V0=+0.3300, V1=+0.8400, dV=4.0800, R=1.401e-06 m/V
13.2V group4: p=19, V0=+0.5300, V1=-0.3100, dV=6.7200, R=8.977e-07 m/V
13.2V group5: p=18, V0=+0.3500, V1=+0.8400, dV=3.9200, R=1.458e-06 m/V
13.2V group6: p=18, V0=+0.5300, V1=-0.2500, dV=6.2400, R=9.159e-07 m/V


--- Final results (mean ± SEM) ---
5.00 Vpp:  R = (1.23 ± 0.11) × 10^-6 m/V
13.2 Vpp:  R = (1.18 ± 0.11) × 10^-6 m/V

--- Consistency check ---
|Δ| = 5.479e-08 m/V
σ_combined = 1.516e-07 m/V
z = 0.36  (z<1 => consistent within 1σ)



