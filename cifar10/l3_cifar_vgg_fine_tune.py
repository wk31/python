# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:21:58 2020

@author: 11597
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:16:23 2020

@author: 11597
"""
import tensorflow as tf
import matplotlib.pyplot as plt

mymodel = tf.keras.models.load_model('vgg16_cifar1.h5')


for layer in mymodel.layers[13:19]:
    print(layer)
    layer.trainable = True
print(mymodel.summary())

(x_train,y_train),(x_test,y_test) = tf.keras.datasets.cifar10.load_data()
x_train=x_train/255.0
x_test=x_test/255.0
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(100).batch(64)
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_dataset = test_dataset.batch(64)

mymodel.compile(optimazer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

#history = mymodel.fit_generator(datagen.flow(x_train, y_train, batch_size=32), epochs=3, validation_data=test_dataset)
history = mymodel.fit(train_dataset, epochs=3, validation_data=test_dataset)


mymodel.save("vgg16_cifar2.h5")



mymodel.evaluate(test_dataset)
acc = history.history['sparse_categorical_accuracy']
val_acc = history.history['val_sparse_categorical_accuracy']

loss=history.history['loss']
val_loss=history.history['val_loss']