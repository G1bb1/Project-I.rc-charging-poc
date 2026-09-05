'''
File:
por_circuit.py

Description:
This program draws a power-on-reset (POR) circuit. An RC circuit is drawn where, inbetween
the resistor and capacitor, the wire is connected to the active-low RESET pin of a
microcontroller. The pin is held low during the capacitor charging until it passes
a threshold.

Note:
- At the very end of this file, be aware that the save file path
  is relative to the current working directory.

___________________________________________________
Author      Date                Comment
Gib M.      Sept. 4th, 2026     rev 1
'''

import schemdraw
import schemdraw.elements as elm

# Schematic drawing class object to create an RC circuit illustration
d = schemdraw.Drawing()

# Draws an RC circuit
d += (vcc := elm.Dot().label("$V_{CC}$", loc="left"))
d += elm.Resistor().down().label("$R$")
d += (node := elm.Dot())        # This node is a connected crossing wire to a microcontroller
d += elm.Capacitor().down().label("$C$")
d += elm.Ground()

# Draws the microcontroller reset
d += elm.Line().at(node.start).right().length(1.5)
d += (mcu := elm.Ic(pins=[elm.IcPin(name=r"$\overline{\mathrm{RESET}}$" + "\n(active low)",side="left")],
    size=(3, 2.2),).anchor("inL1").label("MCU", loc="top"))   # This describes an active low RESET pin

# Paths are relative to the repository root (run the script from there)
#d.save("figures/por_circuit.pdf")
d.save("../../figures/generated/por_circuit.pdf")