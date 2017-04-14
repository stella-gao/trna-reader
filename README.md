# trna-reader
A project to see if recurrent neural networks can learn to write transcribe tRNA

## Installing Everything
Because of limited support for different operating systems in the bioconda packages, only Linux support is tested. Other operating systems may be used, but are not officially supported.

### Anaconda Packages
```
conda env create -f environment.yml
source activate trna-reader
```

### Environment PyPi Packages
Make sure to do this within the newly created Anaconda environment.

```
pip install -r requirements.txt
```

### Running
To view the Jupyter notebook, please use
```
jupyter notebook
```
while within the trna-reader anaconda environment.


# The Prospect of Using rFAM or Infernal

A [Python binding](https://anaconda.org/bioconda/infernal) for [Infernal](http://eddylab.org/infernal/) can be found hosted as a package on the [bioconda](https://bioconda.github.io/).

Infernal is created by the [Eddy/Rivas Lab](http://eddylab.org/) ([Github]()) formerly at the Janelia Institute and now at Harvard University.

[rFam](http://rfam.readthedocs.io/en/latest/index.html) can be used for looking for families of RNA sequences.

