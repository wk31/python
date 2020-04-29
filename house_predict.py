# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:23:52 2020

@author: 11597
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

def MAE_loss(y,y_hat):
    return np.mean(np.abs(y-y_hat))

def MSE_loss(y, y_hat):
    return np.mean(np.square(y_hat-y))

def Linear(x, W, b):
    y=x.dot(W)+b
    return y

def Relu(x):
    result = np.where(x<0, 0, x)
    return result




boston_data = load_boston()
x = boston_data.data
y = boston_data.target
#数据预处理
max_x = np.max(x)
max_y = 1
#x = x/max_x
x = (x-np.mean(x, axis=0))/np.std(x, axis = 0)
y = y/max_y
x_train,y_train,x_target,y_target = train_test_split(x, y, test_size = 0.25)
y=y.reshape(y.shape[0], 1)
x_target = x_target.reshape(x_target.shape[0], 1)
y_target = y_target.reshape(y_target.shape[0], 1)

n_features = x.shape[1]
n_hidden = 10
#参数初始化
w1=np.random.randn(n_features, n_hidden)
b1=np.zeros(n_hidden)
w2=np.random.rand(n_hidden,1)
b2=np.zeros(1)



learning_rate = 0.000001 
train_time=3000
loss=[]
loss2=[]
for i in range(train_time):
#    前向传播
    L1=Linear(x_train, w1, b1)
    s1 = Relu(L1)
    y_pred = Linear(s1, w2, b2)
    
#    计算损失
    loss.append(MSE_loss(x_target,y_pred))
    
#    反向传播
    grad_y_pred = 2.0*(y_pred-x_target)
    grad_w2 = s1.T.dot(grad_y_pred)
    grad_relu = grad_y_pred.dot(w2.T)
    grad_relu[L1<0]=0
    grad_w1 = x_train.T.dot(grad_relu)
    
#    权重更新
    w1 = w1 - learning_rate *grad_w1
    w2 = w2 - learning_rate *grad_w2
#    if train_time%100==0:
#        print(loss)
    
    
    L1_p = Linear(y_train, w1, b1)
    s1_p = Relu(L1_p)
    y_pred_p = Linear(s1_p, w2, b2)
#    print(y_target-y_pred_p)
    loss2.append(MSE_loss(y_target,y_pred_p))

import matplotlib.pyplot as plt
plt.plot(loss)
plt.plot(loss2)





    
    







