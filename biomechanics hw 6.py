# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:14:50 2021

@author: lukem
"""
import numpy as np
import matplotlib.pyplot as plt

Lambda = np.arange(1.05,1.75,.05)
sigma = np.array([.2, .45, .9, 2.4, 4.1, 6.15, 8.55, 11.5, 15.15, 19.75, 25.8, 34.1, 46.2, 65.4])

Y = sigma / (2*(Lambda - Lambda**(-2)))
X = (1 - Lambda**(-3)) / (Lambda - Lambda**(-2))

C2, C1 = np.polyfit(X, Y, 1) 

plt.plot(X, Y, '--o',label='Mooney Material Plot')
plt.plot(X, C1 + C2*X, 'r-', label='Line of Best Fit')
plt.title('Mooney Material Coefficients')
plt.legend()

epslion = Lambda - 1
Y = np.log(sigma)
X = np.log(epslion)

beta, lnA = np.polyfit(X, Y, 1)
plt.figure()
plt.plot(X, Y, '--o',label='Mooney Material Plot')
plt.plot(X, lnA + beta*X, 'r-', label='Line of Best Fit')
plt.title('  Coefficients')
plt.legend()