from retrieve_fasta import getSequences

import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop

sequences = getSequences()
print(sequences)

chars = ['A', 'C', 'G', 'T']
chars2index = dict((c, i) for i, c in enumerate(chars))

# how much we tell the rnn before it has to guess
test_length = 25
step = 3

# list of all the tests, semiredundant
test_sequences = []
next_bases = []

for seq in sequences:
    for i in range(0, len(seq) - test_length, step):
        test_sequences.append(seq[i: i + test_length])
        next_bases.append(seq[i + test_length])

# turn into vectors
# first dimension - each test case
# second dimension - number of hints to give
# third dimension - boolean representation for chars
X = np.zeros((len(test_sequences), test_length, len(chars)), dtype=np.bool)
y = np.zeros((len(next_bases), len(chars)), dtype=np.bool)

for i, seq in enumerate(test_sequences):
    for t, char in enumerate(seq):
        X[i, t, chars2index[char]] = 1
    y[i, chars2index[next_bases[i]]] = 1

print('Build the single LSTM model...')
model = Sequential()
model.add(LSTM(128, input_shape=(test_length, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01))

for i in range(10):
    print('round %i' % i)
    model.fit(X, y, batch_size=128, epochs=1)

pred = model.predict(X[0:1])

print(pred, flush=True)
