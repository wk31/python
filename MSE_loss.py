# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:08:46 2020

@author: 11597
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,2,3,4,5])
y = np.array([1,3,3,5,2])
plt.scatter(x,y)

plt.grid()
plt.show()


def MAE_loss(y, y_hat):
    return np.mean(np.abs(y_hat-y))

def MSE_loss(y, y_hat):
    return np.mean(np.square(y_hat-y))


y_hat = np.array([-2,-2,-1,3,5])
print(MAE_loss(y,y_hat))
print(MSE_loss(y,y_hat))

def linear(x,k,b):
    y = k*x+b
    return y

min_loss = float('inf')

for k in np.arange(-2,2,0.1):
    for b in np.arange(-10,10,0.1):
        y_hat = [linear(xi,k,b) for xi in list(x)]
        current_loss = MAE_loss(y,y_hat)
        mse_loss = MSE_loss(y,y_hat)
        if current_loss<min_loss:
            min_loss = current_loss
            b_k,b_b= k, b
            print(k,b)
            print(min_loss)
#        print(current_loss)
        
y_hat = b_k*x+b_b
plt.scatter(x,y)
plt.plot(x,y_hat,color='red')
plt.grid()
plt.show()

