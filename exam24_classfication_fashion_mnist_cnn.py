# -*- coding: utf-8 -*-
"""exam24_classfication_fashion_mnist_CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C6cmCxV9PriY8qeuQOUmgKoUi7U0okKb
"""

import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from tensorflow.keras import datasets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout
from tensorflow.keras.optimizers import Adam

(X_train, Y_train), (X_test, Y_test) = datasets.fashion_mnist.load_data()
print(X_test.shape, Y_test.shape)

label = ['T-shirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']

my_sample = np.random.randint(60000)
plt.imshow(X_train[my_sample], cmap='gray')
plt.show()
print(label[Y_train[my_sample]])

y_train = np_utils.to_categorical(Y_train)
y_test = np_utils.to_categorical(Y_test)

print(Y_train[0])
print(y_train[0])

x_train = X_train / 255
x_test = X_test / 255
x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
print(x_train.shape)

model = Sequential()
model.add(Conv2D(32, input_shape=(28,28,1), activation='relu', kernel_size=(3,3), padding='same'))
model.add(MaxPool2D(padding='same', pool_size=(2, 2)))
model.add(Conv2D(32, input_shape=(28,28,1), activation='relu', kernel_size=(3,3), padding='same'))
model.add(MaxPool2D(padding='same', pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))
opt = Adam(learning_rate=0.01)
model.compile(opt, loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

fit_hist = model.fit(x_train, y_train, batch_size=480, epochs=15, validation_split=0.2, verbose=1)

score = model.evaluate(x_test, y_test, verbose=0)
print('Final test set accuracy :', score[1])

plt.plot(fit_hist.history['accuracy'])
plt.plot(fit_hist.history['val_accuracy'])
plt.show()

my_sample = np.random.randint(10000)
plt.imshow(X_test[my_sample], cmap='gray')
print(label[Y_test[my_sample]])
pred = model.predict(x_test[my_sample].reshape(-1, 28, 28, 1))
print(pred)
print(label[np.argmax(pred)])
