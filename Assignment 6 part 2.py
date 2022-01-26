# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:03:26 2021

@author: lukem
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data=pd.read_csv('Assignment6_point2_Fs-1000Hz_level-4.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=1000# Sampling frequency in Hz | this value is in the file name 
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Level 4')

from scipy.signal import welch
plt.figure()
plt.hist(signal, 20, density=True)
plt.xlabel('Range')
plt.ylabel('Density')
plt.title('Level 4')
f, Pxx_spec=welch(signal, Fs, nperseg=1000, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Level 4')

data=pd.read_csv('Assignment6_point2_Fs-1000Hz_level-3.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=1000# Sampling frequency in Hz | this value is in the file name 
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Level 3')

from scipy.signal import welch
plt.figure()
plt.hist(signal, 20, density=True)
plt.xlabel('Range')
plt.ylabel('Density')
plt.title('Level 3')
f, Pxx_spec=welch(signal, Fs, nperseg=1000, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Level 3')

data=pd.read_csv('Assignment6_point2_Fs-1000Hz_level-2.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=1000# Sampling frequency in Hz | this value is in the file name 
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Level 2')

from scipy.signal import welch
plt.figure()
plt.hist(signal, 20, density=True)
plt.xlabel('Range')
plt.ylabel('Density')
plt.title('Level 2')
f, Pxx_spec=welch(signal, Fs, nperseg=1000, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Level 2')

data=pd.read_csv('Assignment6_point2_Fs-1000Hz_level-1.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=1000# Sampling frequency in Hz | this value is in the file name 
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Level 1')

from scipy.signal import welch
plt.figure()
plt.hist(signal, 20, density=True)
plt.xlabel('Range')
plt.ylabel('Density')
plt.title('Level 1')
f, Pxx_spec=welch(signal, Fs, nperseg=1000, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Level 1')