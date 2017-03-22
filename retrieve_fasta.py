import urllib.request

x = urllib.request.urlopen('http://gtrnadb.ucsc.edu/genomes/eukaryota/Scere3/sacCer3-tRNAs.fa')
print(x.read())
