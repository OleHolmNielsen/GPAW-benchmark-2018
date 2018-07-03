from math import pi
import numpy as np
from ase.build import mx2
from gpaw import GPAW, Davidson

# Create tube of MoS2:
atoms = mx2('MoS2', size=(3, 2, 1))
atoms.cell[1, 0] = 0
atoms = atoms.repeat((1, 10, 1))
p = atoms.positions
p2 = p.copy()
L = atoms.cell[1, 1]
r0 = L / (2 * pi)
angle = p[:, 1] / L * 2 * pi
p2[:, 1] = (r0 + p[:, 2]) * np.cos(angle)
p2[:, 2] = (r0 + p[:, 2]) * np.sin(angle)
atoms.positions = p2
atoms.cell = [atoms.cell[0, 0], 0, 0]

# setup calculator
kpoints = (4, 1, 1)
atoms.center(vacuum=6, axis=[1, 2])
atoms.pbc = True
tag = 'MoS2-benchmark'
atoms.calc = GPAW(gpts=(48, 168, 168),
                  eigensolver=Davidson(2),
                  xc='PBE',
                  txt=tag + '.txt',
                  kpts={'size': kpoints},
                  nbands='120%')
forces = atoms.get_forces()
