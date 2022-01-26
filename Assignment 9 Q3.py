# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:05:41 2021

@author: lukem
"""
"""Question 3"""

import wave
import numpy as np 
import matplotlib.pyplot as plt
import IPython.display as ipd
from scipy.signal import welch, bessel, filtfilt

"""Extract Signal"""
audio_object=wave.open('Assignment9_point3.wav','r')
number_samples=audio_object.getnframes() #number of samples in file
rate=audio_object.getframerate() # sampling rate (in Hz)
data=np.frombuffer(audio_object.readframes(number_samples), dtype=np.int16) #data as a numpy array
time=np.arange(0,(number_samples-1)*(1/rate),(1/rate)) # time vector as a numpy array
audio_object.close()

"""Plotting Original Audio Signal"""
plt.plot(time,data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')

"""Plotting Power Spectrum"""
f1, Pxx_spec1 = welch(data, rate, nperseg=1000, scaling='spectrum')
plt.figure()
plt.plot(f1, np.sqrt(Pxx_spec1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Power Spectrum')

"""Filtering Signal"""
Ny_freq = 2*rate
cutoff_freq = 10000
num, den = bessel(N=2, Wn=cutoff_freq/Ny_freq, btype='lowpass')
filtered_data = filtfilt(num, den, data)

new_rate=8000# Hz
subsample_data=filtered_data[::int(rate/new_rate)]

"""Plotting Filtered Power Spectrum"""
f2, Pxx_spec2 = welch(subsample_data, rate, nperseg=1000, scaling='spectrum')
plt.figure()
plt.plot(f2, np.sqrt(Pxx_spec2))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Power Spectrum')

ipd.Audio(subsample_data, rate=new_rate)
