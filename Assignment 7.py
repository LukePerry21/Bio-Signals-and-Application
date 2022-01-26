# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:38:39 2021

@author: lukem
"""

import numpy as np
import matplotlib.pyplot as plt

def convolve_sum(x_n,h_n):#This defines the function with 2 inputs (x_n,h_n)
    """ This function assumes that H and X are both at the same starting point
        and that if the point is not defined it is zero"""
        
        

    """ First we must make the inputs into arrays if not already"""
    x_n = np.array(x_n)
    h_n = np.array(h_n)
    
    """ X and H must be made the same size. If they are not the same size,
        the if statements check that then add zeros to make them the same size"""
        
    if len(x_n)<len(h_n):
        x_n = np.append(x_n, np.zeros(len(h_n)-len(x_n)))
    if len(x_n)>len(h_n):
        x_n = np.append(x_n, np.zeros(len(x_n)-len(h_n)))
    
    """ X and H are then padded"""
    x_n = np.append(x_n, np.zeros(len(x_n)+len(h_n)))
    h_n = np.append(h_n, np.zeros(len(x_n)+len(h_n)))
    
    """ The H vector is flipped since the equation is h[-k+n]"""
    h_flipped = np.flip(h_n)
    
    """ An empty array is made to obtain the sum signal Y"""
    y = np.zeros_like(x_n)
    
    """ This For loop calculates the sum based on the equation"""
    for n in range(len(y)):
        for k in range(len(x_n)):
            if k-n<len(h_flipped):
                y[n] = y[n] + h_flipped[k-n-1]*x_n[k]
                #Because the H array is flipped, you must subtract n+1 instead of adding n
           

    return y

""" Test from example given"""
x = [.5,2]
h = [1,1,1]

y = convolve_sum(x,h)
y_test = np.convolve(x, h)

plt.plot(y,'x', markersize=8)
plt.plot(y_test,'o', markersize=4)

""" Secondary test from random arrays"""
plt.figure()
x = [2,1,4,85,35,3,2,4,6]
h = [1,1,1,9,3,6,13,56,34,56]

y = convolve_sum(x,h)
y_test = np.convolve(x, h)

plt.plot(y,'x', markersize=8)
plt.plot(y_test,'o', markersize=4)


