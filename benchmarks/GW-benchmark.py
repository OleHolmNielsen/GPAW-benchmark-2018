from gpaw import GPAW, PW, FermiDirac
from gpaw.response.g0w0 import G0W0
from ase.build import mx2
from ase.parallel import world
from pathlib import Path


def get_bandrange(calc):
    """lower and upper band range
    """
    # bands (-8,4)
    lb, ub = max(calc.wfs.nvalence // 2 - 8, 0), calc.wfs.nvalence // 2 + 4
    return lb, ub


def write_gpw_file():
    """write gs dft calculation
    """
    # start by cleaning up a bit
    if world.rank == 0:
        for name in Path().glob('*.npy'):
            Path(name).unlink()

    world.barrier()
    params = dict(
        mode=PW(400),
        xc='PBE',
        basis='dzp',
        kpts={'size': (6, 6, 1), 'gamma': True},
        occupations=FermiDirac(width=0.05))

    slab = mx2('MoSS', '2H', 3.184, 3.127)
    slab.center(vacuum=8, axis=2)
    slab.pbc = (1, 1, 0)
    slab.calc = GPAW(txt='gs.txt', **params)
    slab.get_forces()
    slab.get_stress()
    slab.calc.write('gs.gpw')


def gw_calc(kptsize=12, ecut=200.0, gwg_and_gw=False, gw_only=True):
    """Calculate the gw bandstructure"""

    calc = GPAW('gs.gpw', txt=None)
    kpts = {'size': (kptsize, kptsize, 1), 'gamma': True}

    calc.set(kpts=kpts,
             fixdensity=True,
             txt='gs_gw.txt')
    calc.get_potential_energy()
    calc.diagonalize_full_hamiltonian(ecut=ecut)
    calc.write('gs_gw_nowfs.gpw')
    calc.write('gs_gw.gpw', mode='all')
    lb, ub = get_bandrange(calc)

    calc = G0W0(calc='gs_gw.gpw',
                bands=(lb, ub),
                ecut=ecut,
                ecut_extrapolation=True,
                truncation='2D',
                nblocks=6,
                q0_correction=True,
                filename='g0w0',
                restartfile='g0w0.tmp',
                savepckl=True)

    calc.calculate()


if __name__ == '__main__':
    write_gpw_file()
    gw_calc(kptsize=6, ecut=200)  # cut down size
