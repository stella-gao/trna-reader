# trna-reader
A project to see if recurrent neural networks can learn to write transcribe tRNA

## Installation 
Because of limited support for different operating systems in the bioconda packages, only Linux support is tested. Other operating systems may be used, but are not officially supported.

```
git clone https://github.com/trevortknguyen/trna-reader
cd trna-reader
conda env create -f environment.yml
source activate trna-reader
pip install -r requirements.txt
jupyter notebook
source deactivate
```

# The Prospect of Using rFAM or Infernal

A [Python binding](https://anaconda.org/bioconda/infernal) for [Infernal](http://eddylab.org/infernal/) can be found hosted as a package on the [bioconda](https://bioconda.github.io/).

Infernal is created by the [Eddy/Rivas Lab](http://eddylab.org/) ([Github]()) formerly at the Janelia Institute and now at Harvard University.

[rFam](http://rfam.readthedocs.io/en/latest/index.html) can be used for looking for families of RNA sequences.

