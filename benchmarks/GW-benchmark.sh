#!/bin/bash
#SBATCH --job-name=GW-benchmark
#SBATCH --mail-type=START,END
#SBATCH --partition=xeon24
#SBATCH --output=%x-%j.out
#SBATCH --time=2:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --cpus-per-task=1
#SBATCH --mem=250G

# This is a Slurm batch job script for the GW-benchmark.py benchmark.
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

mpiexec gpaw-python GW-benchmark.py
