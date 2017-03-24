from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
import numpy as np

chars = 4
charList = ['A', 'T', 'C', 'G']

# how much we tell the rnn before it has to guess
test_length = 25

print('Build the single LSTM model...')
model = Sequential()
model.add(LSTM(128, input_shape=(test_length, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01))
