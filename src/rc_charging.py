'''
File:
rc_charging.py

Description:
This program computes and plots the voltage charge of a capacitor in an RC circuit.
A line separating voltage from LOW and HIGH states are drawn. Additionally,
different resistors values were tested to see the time it takes to charge a capacitor.
The goal is to research different resistor choices that best fit the target release value
of the power on circuit.

Note:
- At the very end of this file, be aware that the save file path
  is relative to the current working directory.

___________________________________________________
Author      Date                Comment
Gib M.      Sept. 4th, 2026     rev 1
'''
import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0 # supply voltage (V)
C = 22e-12 # capacitance (22 pF)
R_main = 10e3 # resistance (10 kohm)
R_others = [22e3, 47e3, 100e3] # comparison resistances

def charging(t, R):
    tau = R * C
    return V0 * (1 - np.exp(-t/tau))

# Base the time axis on the slowest (largest R) curve so all are visible
tau_max = max([R_main] + R_others) * C
t = np.linspace(0, 5 * tau_max, 500)

# Solid is reserved for the original R; every other curve gets its own.
# Dash pattern so the plot reads correctly in black and white
styles = ["--", "-", (0, (3, 1, 1, 1, 1, 1))]

fig, ax = plt.subplots()
ax.plot(t, charging(t, R_main), color="black", linewidth=2.5,
        label=f"R={R_main/1e3:.0f} k$\\Omega$ (main)")
for R, style in zip(R_others, styles):
    ax.plot(t, charging(t, R), color="black", linestyle=style, linewidth=2.5,
            label=f"R = {R/1e3:.0f} k$\\Omega$")

V_tau = V0 * (1 - np.exp(-1))
ax.axhline(V_tau, linestyle=":", color="0.4") # dotted reference line
ax.grid(False)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title(f"Capacitor charging (R = {R/1e3:.0f} k$\\Omega$, C = {C*1e12:.0f} pF)")
ax.legend()

# Paths are relative to the repository root (run the script from there)
#fig.savefig("figures/generated/rc_charging.pdf") # vector, publishable
fig.savefig("../figures/generated/rc_charging.pdf") # vector, publishable