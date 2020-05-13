# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:48:15 2020

@author: 11597
"""
from sklearn import linear_model
import random 

clf = linear_model.LinearRegression()
print(dir(linear_model.LinearRegression()))

def generate(x):
    y=2*x+10+random.random()
    return y

train_x = []
train_y = []

for x in range(1000):
    train_x.append([x])
    y=generate(x)
    train_y.append([y])

clf.fit(train_x, train_y)

print(clf.coef_)
print(clf.intercept_)