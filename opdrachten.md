---
title: Optomechanics RP
date: 2026-02-09
tags:
  - school
  - Q5
  - RP
aliases:
  - Opdrachten voorbereiding RP experiment optomechanics
---

# Manual


# Q's

## A1

Q: Derive an expression for $L$ in terms of $λ$ and give the values for $L$ for which there is constructive and destructive interference. Take $n′ = 1$ and $θ′ = 0\deg$

A: $$\delta=\frac{4\pi}{\lambda}L$$
$$P_r=P_i*f$$
$$f=\frac{F\sin^2(\delta/2)}{1+F\sin^2(\delta/2)}$$
$L$ in terms of $\lambda$:
$$L=\frac{\delta\lambda}{4\pi}$$
Constructive interference when $\sin^2(\delta/2)=1$ and destructive when $\sin^2(\delta/2)=0$

$$\sin^2(\delta/2)=1\implies \delta/2=\pi/2 + k\pi\; \text{ for }k\in\mathbb{Z}$$
$$\sin^2(\delta/2)=0\implies \delta/2=k\pi\; \text{ for }k\in\mathbb{Z}$$
Meaning:
$$\begin{align}
\text{Constructive int. }L&=\frac{\lambda(1+2k)}{4}\\
\text{Destructive int. }L&=\frac{k\lambda}{2}
\end{align}$$
## B1

Beam formula:
$$\begin{align}EI_z\frac{\partial^4Z(x,t)}{\partial x^4}+\rho A\frac{\partial^2Z(x,t)}{\partial t^2}&=0\\
Z(x,t)&=u(x)e^{i\omega t}\\
\frac{\partial^4Z(x,t)}{\partial x^4} &= u''''(x)e^{i\omega t}\\
\frac{\partial^2Z(x,t)}{\partial t^2}&=u(x)\cdot -\omega^2e^{i\omega t}\\
EI_zu''''(x)e^{i\omega t}-\rho Au(x)\cdot \omega^2e^{i\omega t}&=0\\
EI_zu''''(x)e^{i\omega t}&=\rho Au(x)\cdot \omega^2e^{i\omega t}\\
u''''(x)-\frac{\rho A \omega^2}{EI_z}u(x)&=0 \\
k^4&=\frac{\rho A \omega^2}{EI_z} \\
\omega(k)=k^2\sqrt{\frac{EI_z}{\rho A}}
\end{align}$$


