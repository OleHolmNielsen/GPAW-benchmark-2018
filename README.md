# GPAW-benchmark-2018

GPAW code building instructions and benchmark data
--------------------------------------------------

The purpose of this project is to document the building of the
[GPAW](https://wiki.fysik.dtu.dk/gpaw/) code version 1.4.
Subsequently a GPAW test and a GPAW benchmark run is documented.

We require using the [EasyBuild](https://github.com/hpcugent/easybuild)
software build and installation framework that allows you to manage
(scientific) software on High Performance Computing (HPC) systems
in an efficient way.
These instructions are based upon EasyBuild version 3.6.1.

In order to have a well-defined and reproducible software modules framework 
for the purpose of comparing benchmark results obtained on different systems,
we require the use of specific software module toolchains 
provided by EasyBuild version 3.6.1.
Future versions of EasyBuild will contain newer toolchains in addition to
the ones used in the present instruction.

The benchmark requires to build the GPAW code using one or both of the following 
EasyBuild software module toolchains:

1. foss-2018a: BLACS, FFTW, GCC, OpenBLAS, OpenMPI, ScaLAPACK

2. iomkl-2018a: OpenMPI, icc, ifort, imkl

Step 1: Installing Lmod
-----------------------

A software modules tool is a prerequisite, and the recommended tool is
[Lmod](https://www.tacc.utexas.edu/research-development/tacc-projects/lmod).

Brief Lmod installation instructions for CentOS 7 may be found in
https://wiki.fysik.dtu.dk/niflheim/EasyBuild_modules#install-lmod
summarized as:

```
yum install epel-release
yum install Lmod
```

A non-root user can install Lmod as documented in http://easybuild.readthedocs.io/en/latest/Installing-Lmod-without-root-permissions.html

Step 2: Installing EasyBuild
----------------------------

Now EasyBuild should be installed as a normal user.
Brief EasyBuild installation instructions for CentOS 7 may be found in
https://wiki.fysik.dtu.dk/niflheim/EasyBuild_modules

There is an [EasyBuild installation](https://easybuild.readthedocs.io/en/latest/Installation.html) 
guide with detailed instructions.

Define the top-level directory and modules tool for your modules, for example:

```
mkdir $HOME/modules
export EASYBUILD_PREFIX=$HOME/modules
export EASYBUILD_MODULES_TOOL=Lmod
```

Download and install EasyBuild:

```
curl -O https://raw.githubusercontent.com/hpcugent/easybuild-framework/develop/easybuild/scripts/bootstrap_eb.py
python bootstrap_eb.py $EASYBUILD_PREFIX
```

Update $MODULEPATH, load the EasyBuild module, and check the basic functionality:

```
module use $EASYBUILD_PREFIX/modules/all
module load EasyBuild
module list
eb --version
```

Step 3: Build the foss-2018a toolchain
--------------------------------------

EasyBuild version 3.6.1 (and later) contains the foss-2018a toolchain
which is used to build GPAW.
The foss toolchain contains the following modules:

```
BLACS, FFTW, GCC, OpenBLAS, OpenMPI, ScaLAPACK
```

To build the foss-2018a toolchain run this command:

```
eb foss-2018a.eb -r
```

The building of GCC, OpenMPI and FFTW will particularly time consuming,
and this task may take several hours!

Now the foss toolchain modules can be loaded:

```
$ module load foss/2018a
$ module list

Currently Loaded Modules:
  1) GCCcore/6.4.0
  2) binutils/2.28-GCCcore-6.4.0
  3) GCC/6.4.0-2.28
  4) numactl/2.0.11-GCCcore-6.4.0
  5) hwloc/1.11.8-GCCcore-6.4.0
  6) OpenMPI/2.1.2-GCC-6.4.0-2.28
  7) OpenBLAS/0.2.20-GCC-6.4.0-2.28
  8) gompi/2018a
  9) FFTW/3.3.7-gompi-2018a
 10) ScaLAPACK/2.0.2-gompi-2018a-OpenBLAS-0.2.20
 11) foss/2018a
```

Step 4: Build the iomkl-2018a toolchain (optional)
--------------------------------------------------

EasyBuild version 3.6.1 (and later) contains the iomkl-2018a toolchain
which is used to build GPAW.
The iomkl toolchain contains the following modules:

```
OpenMPI, icc, ifort, imkl
```

The Intel compilers icc and ifort, and the MKL library, are products
offered by Intel.
We do not require the use of Intel MPI.

Usage of Intel compiler licenses may find useful hints in the web page
https://wiki.fysik.dtu.dk/niflheim/EasyBuild_modules#intel-compiler-toolchains
To use your Intel <license-server> host port 28518:

```
export INTEL_LICENSE_FILE=28518@<license-server>
```

To build the iomkl-2018a toolchain first install the compiler tar-ball files
as described in 
https://wiki.fysik.dtu.dk/niflheim/EasyBuild_modules#intel-compiler-toolchains

Then run this command:

```
eb iomkl-2018a.eb -r
```

Now the iomkl toolchain modules can be loaded:

```
$ module load iomkl/2018a
$ module list

Currently Loaded Modules:
  1) GCCcore/6.4.0
  2) binutils/2.28-GCCcore-6.4.0
  3) icc/2018.1.163-GCC-6.4.0-2.28
  4) ifort/2018.1.163-GCC-6.4.0-2.28
  5) iccifort/2018.1.163-GCC-6.4.0-2.28
  6) numactl/2.0.11-GCCcore-6.4.0
  7) hwloc/1.11.7-GCCcore-6.4.0
  8) OpenMPI/2.1.2-iccifort-2018.1.163-GCC-6.4.0-2.28
  9) iompi/2018a
 10) imkl/2018.1.163-iompi-2018a
 11) iomkl/2018a
```
