# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:24:13 2021

@author: lukem
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
data=pd.read_csv('Assignment6_point1_Fs-1000Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=1000# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('1000 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=1000, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('1000 Hz')


data=pd.read_csv('Assignment6_point1_Fs-500Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=500# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('500 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=500, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('500 Hz')

data=pd.read_csv('Assignment6_point1_Fs-200Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=200# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('200 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=200, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('200 Hz')

data=pd.read_csv('Assignment6_point1_Fs-111Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=111# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('111 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=111, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('111 Hz')

data=pd.read_csv('Assignment6_point1_Fs-100Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=100# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('100 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=100, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('100 Hz')

data=pd.read_csv('Assignment6_point1_Fs-62Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=62# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('62 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=62, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('62 Hz')

data=pd.read_csv('Assignment6_point1_Fs-52Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=52# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('52 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=52, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('52 Hz')

data=pd.read_csv('Assignment6_point1_Fs-50Hz.csv', index_col=0).to_numpy()
signal=data[:,0] #vector with signal values 
N=len(signal) #lenght of signal
Fs=50# Sampling frequency in Hz | this value is in the file name
Ts=1/Fs# Sampling time
time_vector=np.arange(0, N*Ts,Ts)
plt.figure()
plt.plot(time_vector, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('50 Hz')

from scipy.signal import welch
f, Pxx_spec = welch(signal, Fs, nperseg=50, scaling='spectrum')
plt.figure()
plt.plot(f, np.sqrt(Pxx_spec))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('50 Hz')