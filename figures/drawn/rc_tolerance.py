'''
File:
rc_tolerance.py

Description:
This program quantifies how component tolerance affects the release time of
the ESP32 EN-pin RC power-on-reset. It computes t_release for the nominal R
and C, plus the fastest- and slowest-releasing combinations permitted by
their tolerances, then plots all three charging curves against
V_IH to show the resulting timing spread.

Note:
- At the very end of this file, be aware that the save file path
  is relative to the current working directory.

___________________________________________________
Author      Date                Comment
Gib M.      Sept. 10th, 2026     rev 1
'''
import numpy as np
import matplotlib.pyplot as plt

V0 = 3.3  # ESP32 module typical VDD (V)
VIH = 0.75 * V0  # ESP32 EN pin: VIH min = 0.75*VDD (generic GPIO threshold, applies to EN)

R_nominal = 10_000  # resistance (10 kohm)
C_nominal = 1e-6  # capacitance (1 uF)
tolerance_R = 0.05  # tol for res +-5%
tolerance_C = 0.20  # tol for cap +-20%

# t_release = k*R*C with k = -ln(1 - VIH/V0) > 0, so t_release increases
# monotonically with BOTH R and C: fastest case is smallest R with
# smallest C, slowest case is largest R with largest C.
R_fast, C_fast = R_nominal * (1 - tolerance_R), C_nominal * (1 - tolerance_C)
R_slow, C_slow = R_nominal * (1 + tolerance_R), C_nominal * (1 + tolerance_C)

k = -np.log(1 - VIH / V0)

# Compute t_release
def t_release(R, C):
    return k * R * C

t_nom = t_release(R_nominal, C_nominal)
t_fast = t_release(R_fast, C_fast)
t_slow = t_release(R_slow, C_slow)

t = np.linspace(0, 1.4 * t_slow, 1000)

def V(t, R, C):
    return V0 * (1 - np.exp(-t / (R * C)))

# Plot the charging curve
fig, ax = plt.subplots(figsize=(3.4, 2.6))
ax.plot(t * 1e3, V(t, R_nominal, C_nominal), 'k-',
        label=f'Nominal ($R$={R_nominal / 1e3:.0f} k$\\Omega$, $C$={C_nominal * 1e6:.0f} $\\mu$F)')
ax.plot(t * 1e3, V(t, R_fast, C_fast), 'k--', label='Fastest case ($-$tol on $R,C$)')
ax.plot(t * 1e3, V(t, R_slow, C_slow), 'k-.', label='Slowest case ($+$tol on $R,C$)')
ax.axhline(VIH, color='k', linestyle=':', linewidth=1, label=f'$V_{{IH}}$ = {VIH:.3f} V')
ax.grid(alpha=0.3)
ax.set_xlabel('t (ms)')
ax.set_ylabel('V (V)')
ax.set_title('ESP32 EN-pin POR with tolerance')
ax.legend(fontsize=6, loc='lower right', frameon=False)
fig.tight_layout()

# Paths are relative to the repository root (run the script from there)
#fig.savefig("figures/generated/rc_tolerance.pdf")
fig.savefig("../../figures/generated/rc_tolerance.pdf")