# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:25:46 2021

@author: lukem
"""
"""Question 1"""

import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt
import cmath
import math

Fs=1000# Sampling Frequency [Hz]
duration=30# Signal duration [s]
time=np.arange(0,duration,1/Fs) # time vector

"""Frequencies to be analyzed based on range desired"""
frequencies=np.arange(.1, 20, .2) 

"""Create empty arrays to store magnitude and phase"""
magnitudes=np.zeros_like(frequencies)
phases=np.zeros_like(frequencies)

"""Create arrays for num and den based on equation given"""
num = [10,1]
den = [1,5,200]
system=signal.TransferFunction(num,den)


"""Testing values"""
######
w = 2 * np.pi * frequencies
test_w, test_magnitudes, test_phases = signal.bode(system,w)
######


for index, f in enumerate(frequencies):
    x=np.sin(2*np.pi*f*time)  #input signal

    """Filter input signal""" 
    tout, yout, xout= signal.lsim(system, U=x, T=time ) 

    """Remove the first 5 seconds from input and output"""
    x_short=x[tout>5]
    yout_short=yout[tout>5]
    tout_short=tout[tout>5]             
    
    
    """Magnitude estimation"""
    magnitude = max(yout_short) #Finds the new amplitude of the signal
    magnitude = 20*math.log(magnitude,10) #Calculates Gain of signal 
    
    """Phase estimation"""
    T = tout_short[1]-tout_short[0] #Sampling space
    N = len(yout_short) #Sampling length
    fourier_transform = np.fft.rfft(yout_short) #Calculates fourier transform of output
    fourier_transform = (2/N)*fourier_transform #Normailzes fourier transform
    omega = np.fft.fftfreq(N,T) #Frequency array
    omega = omega[omega >= 0] #Takes out negative frequency
    fourier_transform = fourier_transform[omega >= f] #Makes needed value have index 0
    phase = cmath.phase(fourier_transform[[0]]) #Calculates phase at frequency f
    
    """Saving magnitude and phase"""
    magnitudes[index] = magnitude 
    phases[index] = phase

"""Converting phases calculated to degrees"""
phases = np.rad2deg(phases)

"""Plotting"""   
plt.figure()
plt.semilogx(frequencies, magnitudes)    # Bode magnitude plot
plt.semilogx(frequencies, test_magnitudes, '--')    # Test magnitude plot
plt.title('Magnitude')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain (dB)')
plt.figure()
plt.semilogx(frequencies, phases)  # Bode phase plot
plt.semilogx(frequencies, test_phases, '--')  # Test phase plot
plt.title('Phase')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase (Degrees)')


