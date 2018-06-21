# GPAW-benchmark-2018

GPAW code building instructions and benchmark data
--------------------------------------------------

The purpose of this project is to document the building of the
[GPAW](https://wiki.fysik.dtu.dk/gpaw/) code version 1.4.

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

Step 1: Installing EasyBuild
----------------------------

There is an [EasyBuild installation](https://easybuild.readthedocs.io/en/latest/Installation.html) 
guide with detailed instructions.

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

Now EasyBuild should be installed as a normal user.
Brief EasyBuild installation instructions for CentOS 7 may be found in
https://wiki.fysik.dtu.dk/niflheim/EasyBuild_modules

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
