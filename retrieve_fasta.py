import urllib.request


x = urllib.request.urlopen('http://gtrnadb.ucsc.edu/genomes/eukaryota/Scere3/sacCer3-tRNAs.fa')
content = x.read().decode("utf-8")
# now we have a list of the lines in the file
lines = content.split('\n')

print(len(lines))

sequences = []
seq_index = -1
for i in range(len(lines)):
    if lines[i].startswith('>'):
        seq_index += 1
        sequences.append('>')
    else:
        sequences[seq_index] += lines[i]

print(sequences)
print(len(sequences))

# how much we tell the rnn before it has to guess
test_length = 25

# map the chars to numbers to feed in
chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))
# we have a forward-backward map of the chars to indices
