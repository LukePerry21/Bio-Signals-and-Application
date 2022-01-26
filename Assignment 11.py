# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:35:35 2021

@author: lukem
"""

import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt

"""Part A"""

num = [1]
den = [1,100,.4]
continuous_system = signal.TransferFunction(num,den)
w, mag, phase = signal.bode(continuous_system)

plt.figure()
plt.semilogx(w, mag, label='Continuous')
plt.title('Frequency Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain (dB)')

"""From the plot we can see that this system acts as a 
lowpass filter with a cutoff frequency around 10^-2"""


"""Part C"""
T_vals = [1/5, 1/10, 1/50, 1/100, 1/1000] #sampling rate values
for t in T_vals:
    #Create num and den array based on work in part b
    num = [t**2, 2*t**2, t**2]
    den = [4 + 200*t - .4*(t**2), -8 - .8*(t**2), 4 - 200*t - .4*(t**2)]
    discrete_system = signal.TransferFunction(num, den, dt=t)
    w, mag, phase=signal.dbode(discrete_system)
    plt.semilogx(w, mag, label='T='+str(t))
    plt.legend()    
    
plt.show()   
    
"""
The graphs show that the discrete frequency response is 
similar to the continuous frequency response for a given range of frequency
but is unable to capture the full range of frequencies the continuous response is 
able to filter.
"""