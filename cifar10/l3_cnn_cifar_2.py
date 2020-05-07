# -*- coding: utf-8 -*-
"""
Created on Fri May  1 08:53:20 2020

@author: 11597
"""

import tensorflow as tf
import matplotlib.pyplot as plt
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.cifar10.load_data()
#for i in range(1,11):
#    plt.subplot(2,5,i)
#    plt.imshow(x_train[i-1])
#    plt.text(3,10,str(y_train[i-1]))
#    plt.xticks([])
#    plt.yticks([])
#    print(y_train[i-1])
#plt.show()

#1. 图像加载
#x_train=x_train/255.0
x_test=x_test/255.0
#train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
#train_dataset = train_dataset.shuffle(100).batch(64)
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_dataset = test_dataset.batch(64)

datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True)

model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(32,32,3)),
        tf.keras.layers.Conv2D(32, 3, padding='same', activation = 'relu'),
        tf.keras.layers.Conv2D(64, 3, padding='same', activation = 'relu'),
        tf.keras.layers.AveragePooling2D(),
        tf.keras.layers.Conv2D(64, 1, padding='same', activation = 'relu'),
        tf.keras.layers.Conv2D(128, 3, padding='same',activation = 'relu'),
        tf.keras.layers.Conv2D(64, 1, padding='same', activation = 'relu'),
        tf.keras.layers.AveragePooling2D(),
         tf.keras.layers.Conv2D(64, 1,padding='same', activation = 'relu'),
         tf.keras.layers.Conv2D(128, 3,padding='same', activation = 'relu'),
         tf.keras.layers.Conv2D(64, 1,padding='same', activation = 'relu'),
         tf.keras.layers.AveragePooling2D(),
         tf.keras.layers.Conv2D(64, 3,padding='same', activation = 'relu'),
         tf.keras.layers.Conv2D(32, 3,padding='same', activation = 'relu'),
         tf.keras.layers.Flatten(),
         tf.keras.layers.Dropout(rate=0.5),
        tf.keras.layers.Dense(64, activation = 'relu'),
        tf.keras.layers.Dense(10, activation = 'softmax')

                ])


model.compile(optimazer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

history = model.fit_generator(datagen.flow(x_train, y_train, batch_size=32), epochs=15, validation_data=test_dataset)
print(history)
#model.evaluate(test_dataset)
#acc = history.history['accuracy']
#val_acc = history.history['val_accuracy']
#
loss=history.history['loss']
val_loss=history.history['val_loss']
#
#epochs_range = range(15)
#
#plt.figure(figsize=(8, 8))
#plt.subplot(1, 2, 1)
#plt.plot(epochs_range, acc, label='Training Accuracy')
#plt.plot(epochs_range, val_acc, label='Validation Accuracy')








