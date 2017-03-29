# trna-reader
A project to see if recurrent neural networks can learn to write transcribe tRNA

## Installing Everything

### Anaconda Packages
* numpy
* scipy
* biopython (may come in later)

### Environment PyPi Packages
* tensorflow
* keras

## Windows Installation
We have to use Python 3.5 because Tensorflow for Windows only supports Python 3.5 for now.

If you have an nVidia graphics card, then you can use ```pip install tensorflow-gpu```, but if not, you have to stick with ```pip install tensorflow```.
```
conda create -n trna-env python=3.5
activate trna-env
conda install numpy scipy
pip install tensorflow keras
```

# Miscellaneous Things

## Using Anaconda to Manage Packages
Because BARNACLE is a Python 2.7 library, the project has to run in Python 2.7. The only problem is that Tensorflow only supports Python 3.5 right now. I was debating whether or not to even use BARNACLE because the project seems to be inactive, however porting the code to Python 3 would still be an option.

In order to install Barnacle to an Anaconda environment:
```
source activate trna-env
pip install /path/to/barnacle/download/ --target /path/to/anaconda/environment
```

## BARNACLE stuff
So BARNACLE is going to be the program that turns the tRNA predictions into tertiary structures! It's going to add some more requirements to the project. Unfortunately, the BARNACLE project seems a little dead, but it's all that I can get for now.

BARNACLE requires biopython in order to manage pdb files and it also needs numpy, which is something we already have.

## PyMol Issues
For some reason, I can't get PyMol to install on any system other than Windows. I keep getting "segmentation fault" on my Debian-based systems. I would really like to use PyMol because it would integrate well with my Python-based project.

I am currently looking at VMD (Visual Molecular Dynamics) as an alternative, but I will be using PyMol on Windows for now.
