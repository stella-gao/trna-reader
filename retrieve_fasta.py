import urllib.request

def getSequences():
    x = urllib.request.urlopen('http://gtrnadb.ucsc.edu/genomes/eukaryota/Scere3/sacCer3-tRNAs.fa')
    content = x.read().decode("utf-8").upper()
    # now we have a list of the lines in the file
    lines = content.split('\n')

    sequences = []
    seq_index = -1
    for i in range(len(lines)):
        if lines[i].startswith('>'):
            seq_index += 1
            sequences.append('')
        else:
            sequences[seq_index] += lines[i]

    return sequences
