#!/bin/bash
#SBATCH --job-name=Ru2Cl6-benchmark
#SBATCH --mail-type=START,END
#SBATCH --partition=xeon24
#SBATCH --output=%x-%j.out
#SBATCH --time=6:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --cpus-per-task=1
#SBATCH --mem=250G

# This is a Slurm batch job script for the Ru2Cl6-benchmark.py benchmark.
# It is assumed that a GPAW 1.4 software module can be loaded.

echo Hostname: `hostname`
echo CPU type:
lscpu

# Select EasyBuild toolchain:
export TOOLCHAIN=foss-2018a
# export TOOLCHAIN=iomkl-2018a

module purge
module load GPAW/1.4.0-$TOOLCHAIN-Python-3.6.4
module list

# Run 1 thread per task
export OMP_NUM_THREADS=1

mpiexec gpaw-python Ru2Cl6-benchmark.py

echo Extract numbers for correctness and timing
grep Free Ru2Cl6-benchmark.txt
grep Total: Ru2Cl6-benchmark.txt
