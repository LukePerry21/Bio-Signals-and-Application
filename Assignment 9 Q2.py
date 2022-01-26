# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:01:44 2021

@author: lukem
"""
"""Question 2"""

"""Extract Signal"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

data = pd.read_csv('Assignment9_point2.csv', index_col=0).to_numpy()
time=data[:,0] #vector with time values
signal=data[:,1] #vector with signal values

"""Plot Original Signal and Fourier Transform"""
########################
plt.figure()
plt.plot(time, signal)
plt.title('Original Signal')

N = len(signal)
T = time[1]-time[0]
fourier_transform = np.fft.rfft(signal-np.mean(signal))
fourier_transform = 2/N*fourier_transform
frequency = np.fft.fftfreq(N,T)
frequency = frequency[frequency >= 0]
magnitude = abs(fourier_transform)
plt.figure()
plt.plot(frequency, magnitude)
plt.title('Fourier Transform Magnitude for all frequencies')
fourier_transform = fourier_transform[frequency <= 50]
low_frequency = frequency[frequency <= 50]
magnitude = abs(fourier_transform)
plt.figure()
plt.plot(low_frequency, magnitude)
plt.title('Fourier Transform Magnitude for Low frequencies')



"""Filtering"""
########################
Fs = 1000
highpass_cutoff_freq = 1.5
lowpass_cutoff_freq = 25
b, a = scipy.signal.butter(2, highpass_cutoff_freq, 'hp', analog= False, fs=Fs)
filtered1 = scipy.signal.filtfilt(b, a, signal)
d, c = scipy.signal.butter(2, lowpass_cutoff_freq, 'lp', analog= False, fs=Fs)
filtered2 = scipy.signal.filtfilt(d, c, filtered1)

"""Plot Frequency Response for Lowpass and Highpass Filters"""
########################
freq1, response1 = scipy.signal.freqz(b, a, fs=Fs)
mag1 = 20 * np.log10(abs(response1))
plt.figure()
plt.semilogx(freq1, mag1)
plt.title('Highpass filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude')
plt.grid(which='both', axis='both')
plt.axvline(highpass_cutoff_freq, color='green') # cutoff frequency

plt.figure()
plt.semilogx(freq1, np.angle(response1))
plt.title('Highpass filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [Radians]')
plt.grid(which='both', axis='both')
plt.axvline(highpass_cutoff_freq, color='green') # cutoff frequency

freq2, response2 = scipy.signal.freqz(d, c, fs=Fs)
mag2 = 20*np.log10(abs(response2))
plt.figure()
plt.semilogx(freq2, mag2)
plt.title('Lowpass filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude')
plt.grid(which='both', axis='both')
plt.axvline(lowpass_cutoff_freq, color='green') # cutoff frequency

plt.figure()
plt.semilogx(freq2, np.angle(response2))
plt.title('Lowpass filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [Radians]')
plt.grid(which='both', axis='both')
plt.axvline(lowpass_cutoff_freq, color='green') # cutoff frequency

"""Plot Filtered Signal"""
########################
plt.figure()
plt.plot(time, filtered2)
plt.title('Bandpass Filtered Signal')

N_new = int(N/10)*10
filtered_cut = filtered2[0:N_new]
filtered_segmented = np.reshape(filtered_cut, (10,int(N_new/10)))
filtered_avg = np.mean(filtered_segmented, axis=0)
time_cut = time[0:len(filtered_segmented[1,:])]
plt.figure()
for i in range(10):
    plt.plot(time_cut, filtered_segmented[i,:])
    
plt.title('Single Heart Beat Overlayed')

"""Extra Credit"""
################################
"""Find Peaks"""
peaks, _ = scipy.signal.find_peaks(filtered2, height=1) #Finds any peak above the height of 1
plt.figure()
plt.plot(time,filtered2)
plt.plot(time[peaks], filtered2[peaks], "x")
plt.plot(time,np.ones_like(filtered2), "--", color="gray")
plt.title('Finding Peaks')

"""Finding Time between Heart beats"""
time_between_hb = np.zeros_like(peaks[0:-1],dtype=float) #creates array of zeros with len 1 less than peaks
for ind, pk in enumerate(peaks):
    if ind<len(time_between_hb):
        tbp = time[peaks[ind+1]] - time[peaks[ind]] 
        time_between_hb[ind] = tbp
        #Finds difference in time peaks occur
avg_time_between_hb = np.mean(time_between_hb)
HR = 60/time_between_hb
HR_avg = 60/avg_time_between_hb
plt.figure()
plt.plot(time_between_hb)
plt.hlines(avg_time_between_hb, xmin=0, xmax=len(time_between_hb)-1)
plt.title('Time Between Heart beats (sec)')

plt.figure()
plt.plot(HR)
plt.hlines(HR_avg, xmin=0, xmax=len(HR)-1)
plt.title('Heart Rate (beats per min)')
