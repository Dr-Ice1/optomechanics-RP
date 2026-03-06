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

![[Manual_v6.pdf]]

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
$$\begin{align}
EI_z\frac{\partial^4Z(x,t)}{\partial x^4}+\rho A\frac{\partial^2Z(x,t)}{\partial t^2}&=0\\
Z(x,t)&=u(x)e^{i\omega t}\\
\frac{\partial^4Z(x,t)}{\partial x^4} &= u''''(x)e^{i\omega t}\\
\frac{\partial^2Z(x,t)}{\partial t^2}&=u(x)\cdot -\omega^2e^{i\omega t}\\
EI_zu''''(x)e^{i\omega t}-\rho Au(x)\cdot \omega^2e^{i\omega t}&=0\\
EI_zu''''(x)e^{i\omega t}&=\rho Au(x)\cdot \omega^2e^{i\omega t}\\
u''''(x)-\frac{\rho A \omega^2}{EI_z}u(x)&=0 \\
k^4&=\frac{\rho A \omega^2}{EI_z} \\
\omega(k)=k^2\sqrt{\frac{EI_z}{\rho A}}
\end{align}$$

We can find that:$$\begin{align}a_1=-a_3\\a_2=-a_4\end{align}$$
From $u(0)=0$ and $u'(0)=0$, then simplify all systems to:

$$
\begin{aligned}
u(x) &= a_1(\cosh kx - \cos kx)
      + a_2(\sinh kx - \sin kx) \\[6pt]

u'(x) &= k\Big[
a_1(\sinh kx + \sin kx)
+ a_2(\cosh kx - \cos kx)
\Big] \\[6pt]

u''(x) &= k^2\Big[
a_1(\cosh kx + \cos kx)
+ a_2(\sinh kx + \sin kx)
\Big] \\[6pt]

u'''(x) &= k^3\Big[
a_1(\sinh kx - \sin kx)
+ a_2(\cosh kx + \cos kx)
\Big]
\end{aligned}
$$

Then we can get a system of equations from the fact that $u''(L)=u'''(L)=0$, which leaves us with ($\alpha=kL$):
$$\begin{align}
a_1(\cosh \alpha + \cos \alpha)
+ a_2(\sinh \alpha + \sin \alpha) &= 0 \\[6pt]

a_1(\sinh \alpha - \sin \alpha)
+ a_2(\cosh \alpha + \cos \alpha) &= 0
\end{align}$$

We use our Linear Algebra knowledge to set the determinant to $0$:
$$\det
\begin{pmatrix}
\cosh \alpha + \cos \alpha & \sinh \alpha + \sin \alpha \\
\sinh \alpha - \sin \alpha & \cosh \alpha + \cos \alpha
\end{pmatrix}
= 0$$
which is:

$$
(\cosh \alpha + \cos \alpha)(\cosh \alpha + \cos \alpha)
- (\sinh \alpha + \sin \alpha)(\sinh \alpha - \sin \alpha) = 0
$$

which simplifies to:

$$
\begin{aligned}
&\det
\begin{pmatrix}
\cosh\alpha+\cos\alpha & \sinh\alpha+\sin\alpha \\
\sinh\alpha-\sin\alpha & \cosh\alpha+\cos\alpha
\end{pmatrix}
=0 \\[10pt]

&(\cosh\alpha+\cos\alpha)(\cosh\alpha+\cos\alpha) \\
&\qquad -(\sinh\alpha+\sin\alpha)(\sinh\alpha-\sin\alpha)=0 \\[10pt]

&(\cosh\alpha\cosh\alpha
+\cosh\alpha\cos\alpha
+\cos\alpha\cosh\alpha
+\cos\alpha\cos\alpha) \\
&\qquad -(\sinh\alpha\sinh\alpha
-\sinh\alpha\sin\alpha
+\sin\alpha\sinh\alpha
-\sin\alpha\sin\alpha)=0 \\[10pt]

&\cosh^2\alpha
+2\cosh\alpha\cos\alpha
+\cos^2\alpha
-\sinh^2\alpha\\
&+\sinh\alpha\sin\alpha
-\sin\alpha\sinh\alpha
+\sin^2\alpha
=0\\\\
&\implies 1+\cosh(\alpha)\cos(\alpha)=0
\end{aligned}
$$

![[coshcos.png]]

As we can see in the graph (and is to be expected looking at the function), the function is harmonic. The corresponding values to the blue indicators are:

```txt
Roots in [-50, 50]:
-48.694686130642
-45.553093477052
-42.411500823462
-39.269908169872
-36.128315516283
-32.986722862693
-29.845130209102
-26.703537555518
-23.561944901806
-20.420352251041
-17.278759532088
-14.137168391046
-10.995540734875
-7.854757438238
-4.694091132974
-1.875104068712
1.875104068712
4.694091132974
7.854757438238
10.995540734875
14.137168391046
17.278759532088
20.420352251041
23.561944901806
26.703537555518
29.845130209102
32.986722862693
36.128315516283
39.269908169872
42.411500823462
45.553093477052
48.694686130642
```

