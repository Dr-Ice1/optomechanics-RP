
# A1
python script met volgende grafiek:
![[opdr-A1.png]]


# A2
We did not see a difference when changing the offset, but we should have seen a difference on the oscilloscope because adding an offset is the same of changing the cavity length. This is because the cavity length is in a state of contraction and expansion, and changing the offset means a different voltage going to the peizo. This would change the cavity length which is essentially changing the length manually by adjusting the fiber by hand. We suspect that the peak-to-peak of the signal generator was too high, so the offset only changed it a small bit, which is why we did not observe anything on the oscilloscope.

# A3
## See README
--- Final results (mean ± SEM) ---
5.00 Vpp:  R = (1.23 ± 0.11) × 10^-6 m/V\
13.2 Vpp:  R = (1.18 ± 0.11) × 10^-6 m/V

# A4

By increasing the driving frequency while keeping the input amplitude constant, the output signal amplitude from the optical cavity was observed to decrease above approximately **1 kHz**. The cutoff frequency is defined as the frequency where the amplitude drops by a factor of √2 (−3 dB). From the observed decrease in signal amplitude, the cutoff frequency of the piezo amplifier is estimated to be **fc≈1 kHzf_c \approx 1\,\text{kHz}fc​≈1kHz**.

# B1

![[B1_15kHz.png|215]]![[B1_30kHz.png|214]]![[B1_45kHz.png|213]]
A peak appears in the spectrum at the frequency of the signal generator. This peak corresponds to the vibration of the cantilever detected by the interferometer.

# B2

 ![[Pasted image 20260307214638.png|337]]![[Pasted image 20260308112824.png|344]]
 ![[Pasted image 20260308140152.png|337]]![[Pasted image 20260308140207.png|343]]
The driven frequency response of both cantilevers was measured by sweeping the piezo drive frequency and recording the interferometric amplitude response. For the long cantilever, clear resonance peaks were observed at approximately 16 kHz and 86 kHz, which we identify as the first two flexural modes. For the short cantilever, peaks were observed at approximately 53 kHz and 260 kHz.

For an ideal rectangular cantilever, the resonance frequencies follow the Euler–Bernoulli beam model, with f2/f1≈6.27f_2/f_1 \approx 6.27f2​/f1​≈6.27. Our measured ratios are somewhat lower than this ideal value, which may be caused by non-ideal clamping, damping in air, uncertainty in locating the exact peak center, and coupling to the piezo or chip holder.

Some smaller peaks and shoulders are likely spurious and may originate from mechanical resonances of the mount, the dithering piezo, or optical/electronic artifacts. A control trace in the 250–330 kHz range did not show the same dominant resonance feature, which supports the interpretation that the main peak in that range is related to the cantilever response rather than simple background noise.
# B3

By moving the laser spot along the cantilever while driving at a fixed resonance frequency, the spatial mode shape can be mapped. For the first flexural mode, the amplitude is expected to increase from the clamped end to a maximum at the free end, with no internal node. For the second flexural mode, one internal node is expected, with opposite-phase motion on either side of the node and an antinode near the tip.

# C1

Using the calibration factor from part A, R≈1.2×10−6 m/VR \approx 1.2\times10^{-6}\,\mathrm{m/V}R≈1.2×10−6m/V, the cantilever displacement can be estimated from the oscilloscope peak-to-peak voltage at resonance via

xpp=R Vpp.x_{\mathrm{pp}} = R\,V_{\mathrm{pp}}.xpp​=RVpp​.

For a measured oscilloscope amplitude of Vpp=…V_{\mathrm{pp}}=\dotsVpp​=…, this gives

xpp=…x_{\mathrm{pp}} = \dotsxpp​=…

with an uncertainty obtained from the calibration uncertainty and the oscilloscope reading uncertainty.