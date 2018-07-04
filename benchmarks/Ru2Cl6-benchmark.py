from ase.io import read
from gpaw import GPAW, PW, Davidson, FermiDirac
import numpy as np


def magnetic_atoms(atoms):
    mag_elements = {'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                    'Y', 'Zr', 'Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In',
                    'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl'}
    return np.array([symbol in mag_elements
                     for symbol in atoms.get_chemical_symbols()],
                    dtype=bool)


def get_U_setups(atoms, U):
    if U is None:
        return {}
    is_mag = magnetic_atoms(atoms)
    symbols = atoms.get_chemical_symbols()
    symbols = set([s for s, m in zip(symbols, is_mag) if m])
    setups = {s: ':d,{}'.format(U) for s in symbols}
    return setups


def get_mm(atoms, state):
    ma = magnetic_atoms(atoms)
    if state == 'fm':
        return np.asarray(ma, int)
    elif state == 'afm':
        if sum(ma) % 2 == 0:
            mm = np.zeros(len(ma))
            mm[ma] = 2 * (np.arange(sum(ma)) % 2 - 0.5)
            return mm


def pbeU(tag=None):
    U = 4.0
    ecut = 1200
    kdens = 12
    width = 0.01
    atoms = read('Ru2Cl6-input.json')
    mm = get_mm(atoms, 'afm')
    atoms.set_initial_magnetic_moments(mm)
    xc = 'PBE'
    setups = get_U_setups(atoms, U)
    if tag is None:
        xcstr = 'Ru2Cl6-benchmark'
    else:
        xcstr = 'Ru2Cl6-benchmark' + tag

    calc = GPAW(txt='{}.txt'.format(xcstr),
                mode=PW(ecut),
                eigensolver=Davidson(2),
                setups=setups,
                kpts={'density': kdens, 'gamma': True},
                xc=xc,
                parallel={'augment_grids': True},
                occupations=FermiDirac(width=width),
                convergence={'bands': -4})
    atoms.calc = calc
    atoms.get_potential_energy()
    atoms.calc.write('{}.gpw'.format(xcstr))


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        tag = sys.argv[1]
    else:
        tag = ''
    pbeU(tag=tag)
