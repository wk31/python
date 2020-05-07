# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:27:28 2020

@author: 11597
"""

import tensorflow as tf
import matplotlib.pyplot as plt

conv_base = tf.keras.applications.ResNet101V2(weights='imagenet',  
              include_top=False,        
              input_shape=(32, 32, 3))
conv_base.trainable = False
feature_flatten = tf.keras.layers.Flatten()(conv_base.get_layer('conv4_block23_out').output)
feature_dropout1 = tf.keras.layers.Dropout(0.5)(feature_flatten)
feature_dense1 = tf.keras.layers.Dense(units=512)(feature_dropout1)
feature_dropout2 = tf.keras.layers.Dropout(0.5)(feature_dense1)      
feature_dense2 = tf.keras.layers.Dense(units=62)(feature_dropout2)
feature_class = tf.keras.layers.Dense(units=10, activation='softmax')(feature_dense2) 


mymodel = tf.keras.Model(inputs=conv_base.input, outputs = feature_class)
print(conv_base.summary())



(x_train,y_train),(x_test,y_test) = tf.keras.datasets.cifar10.load_data()
x_train=x_train/255.0
x_test=x_test/255.0
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(100).batch(64)
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_dataset = test_dataset.batch(64)

datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True)









mymodel.compile(optimazer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

#history = mymodel.fit_generator(datagen.flow(x_train, y_train, batch_size=32), epochs=3, validation_data=test_dataset)
history = mymodel.fit(train_dataset, epochs=5, validation_data=test_dataset)


mymodel.save("resnet101_cifar.h5")



mymodel.evaluate(test_dataset)
acc = history.history['sparse_categorical_accuracy']
val_acc = history.history['val_sparse_categorical_accuracy']

loss=history.history['loss']
val_loss=history.history['val_loss']

plt.plot(acc)
plt.plot(val_acc)