# Project.rc-charging-poc

A version-controlled proof of concept modeling RC capacitor charging and its use
in a power-on-reset (POR) circuit, built up alongside a LaTeX research document.

## Structure

```
Project.rc-charging-poc/
|-- README.md
|-- figures/
|   |-- drawn/
|   |   |-- por_circuit.py        # schemdraw schematic of the RC POR network
|   |   `-- rc_tolerance.py       # POR timing under component tolerance
|   `-- generated/
|       |-- por_circuit.pdf
|       |-- rc_tolerance.pdf
|       `-- rc_charging.pdf
|-- report/
|   `-- report.tex                # IEEEtran paper: charging law, POR derivation,
|                                  # applications and limitations
`-- src/
    `-- rc_charging.py            # RC charging model and plot
```

## Building

Run the scripts from the repository root so the figures land at the paths
`report.tex` expects:

```
python3 src/rc_charging.py
python3 figures/drawn/por_circuit.py
python3 figures/drawn/rc_tolerance.py
```

Compile `report/report.tex` with a standard LaTeX toolchain (Overleaf, or
locally with `IEEEtran.cls` installed via `texlive-publishers` on
Debian/Ubuntu).

## Report contents

- Derivation of the RC charging law and the time constant $\tau = RC$.
- Sizing $R$ for a target POR release time, $t_{release} = -RC\ln(1-V_{IH}/V_0)$.
- **Applications and Limitations**: a case study on the EN (CHIP_PU) pin of an
  ESP32 module, whose datasheet calls for exactly this kind of external RC
  network, including a first-order component-tolerance analysis of the
  resulting release-time range.
