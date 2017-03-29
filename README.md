# trna-reader
A project to see if recurrent neural networks can learn to write transcribe tRNA


# BARNACLE stuff
So BARNACLE is going to be the program that turns the tRNA predictions into tertiary structures! It's going to add some more requirements to the project. Unfortunately, the BARNACLE project seems a little dead, but it's all that I can get for now.

BARNACLE requires biopython in order to manage pdb files and it also needs numpy, which is something we already have.


# PyMol Issues
For some reason, I can't get PyMol to install on any system other than Windows. I keep getting "segmentation fault" on my Debian-based systems. I would really like to use PyMol because it would integrate well with my Python-based project.

I am currently looking at VMD (Visual Molecular Dynamics) as an alternative, but I will be using PyMol on Windows for now.

# How to Install Everything that You Need

### Python Modules
* numpy
* keras
* tensorflow

### Anaconda Packages
* numpy
* tensorflow
* biopython

## Using Anaconda to Manage Packages
Because BARNACLE is a Python 2.7 library, the project has to run in Python 2.7.

In order to install Barnacle to an Anaconda environment:
```
source activate my-env
pip install /path/to/barnacle/download/ --target /path/to/anaconda/environment
```
