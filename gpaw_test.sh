#!/bin/bash
#SBATCH --job-name=gpaw-test
#SBATCH --partition=xeon24
#SBATCH --mem=30G
#SBATCH --output=%x-%j.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=Ole.H.Nielsen@fysik.dtu.dk

cd $SLURM_SUBMIT_DIR
echo ===========================================================================
echo "This is output from job: $SLURM_JOBID"
echo "I am here: `hostname -s`:`pwd`"
cat /etc/redhat-release
lscpu
date
echo ===========================================================================
#

# Load the GPAW module
module purge
module load GPAW/1.4.0-foss-2018a-Python-3.6.4
module list

echo Execute GPAW test

# Number of threads must be 1
export OMP_NUM_THREADS=1 

mpirun -np 8 gpaw-python -m gpaw test 

echo Finished GPAW test

module purge
seff $SLURM_JOB_ID
