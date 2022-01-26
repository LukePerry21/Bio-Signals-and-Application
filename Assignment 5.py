# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:48:10 2021

@author: lukem
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Assignment5_point3.csv', index_col=0).to_numpy()
time=data[:,0]  #vector with time 
signal=data[:,1] #vector with signal values

T_len = time[-1]
Ts = time[1]-time[0]
Fs = 1/Ts
N=len(signal)

f1 = 3
f2 = 5
f3 = 11
f4 = 15

plt.figure()
plt.plot(time,signal)  
plt.figure()      
plt.hist(signal)        
X = np.fft.fft(signal)
freq = np.fft.fftfreq(N,Ts)

X_n = (2/N)*X

plt.figure()
plt.plot(freq, abs(X_n))   

time_fix = time[time<3]
N_fix = len(time_fix)
signal_fix = signal[0:N_fix]
X_fix = np.fft.fft(signal_fix)
freq_fix = np.fft.fftfreq(N_fix,Ts)

X_n_fix = (2/N)*X_fix

plt.figure()
plt.plot(freq_fix, abs(X_n_fix),'-o')   
#Number 4
###########################

import matplotlib.pyplot as plt 
import pandas as pd 
data=pd.read_csv('Assignment5_point4.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
plt.figure()
plt.plot(signal)
plt.ylabel('HRV (ms)')
plt.xlabel('Samples')


fourier_transform = np.fft.rfft(signal-np.mean(signal))
abs_fourier_transform = np.abs(fourier_transform)
power_spectrum = np.square(abs_fourier_transform)
frequency = np.linspace(0, 1/2 ,len(power_spectrum))
plt.figure()
plt.plot(frequency, power_spectrum)

signal_segmented=np.reshape(signal,(10,100)) #signal_segmented is a matrix with 10 rows and 100 columns
power_spectrum_segmented = np.empty((10,51))
for i in range(10):
    fourier_transform = np.fft.rfft(signal_segmented[i,:]-np.mean(signal_segmented[i,:]))
    abs_fourier_transform = np.abs(fourier_transform)
    power_spectrum_segmented[i,:] = np.square(abs_fourier_transform)
    frequency_segmented = np.linspace(0, 1/2 ,len(power_spectrum_segmented[i,:]))
    plt.figure()
    plt.plot(frequency_segmented, power_spectrum_segmented[i,:])

ensemble=np.mean(signal_segmented,axis=0)
fourier_transform_ensemble = np.fft.rfft(ensemble-np.mean(ensemble))
abs_fourier_transform_ensemble = np.abs(fourier_transform_ensemble)
power_spectrum_ensemble = np.square(abs_fourier_transform_ensemble)
frequency_ensemble = np.linspace(0, 1/2 ,len(power_spectrum_ensemble))
plt.figure()
plt.plot(frequency_ensemble, power_spectrum_ensemble)

ensemble_partd=np.mean(power_spectrum_segmented,axis=0)
frequency_ensemble = np.linspace(0, 1/2 ,len(power_spectrum_ensemble))
plt.figure()
plt.plot(frequency_ensemble, power_spectrum_ensemble)



