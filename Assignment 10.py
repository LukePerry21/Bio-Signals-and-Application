# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:29:25 2021

@author: lukem
"""

"""Question 1"""
import numpy as np 
import scipy
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt


a_true=[1,-2.2137,2.9403,-2.1697,0.9606] 
# create some data based on these AR parameters
N=1000
e=np.random.randn(N)
y=scipy.signal.lfilter(np.array([1]),a_true,e)
f, Pxx_den = scipy.signal.periodogram(y)

#estimate the model parameters using the Yule-Walker method 
rho, sigma = sm.regression.yule_walker(y, order=4, method='mle')

a_est = np.append(1,-rho)

w, h = scipy.signal.freqz(sigma**2, a_est)
#plot
plt.figure()
plt.plot(f[1:], 10*np.log10((np.abs(Pxx_den[1:]))), )
plt.plot(w/(2*np.pi), 20*np.log10((np.abs(h))), label='AR (4)', lw=4, color='tab:red')
plt.xlabel(r'Normalized Frequency')
plt.ylabel(r'Power/frequency')
plt.title(r'Spectral Density Estimate')
plt.legend()


alpha = [0.1, 0.25, 0.5, 0.75,1]

for a in alpha:
    
    noise = a * np.random.randn(N)
    y_noise = y + noise
    
    plt.figure()
    plt.plot(y,lw=0.5)
    plt.plot(y_noise,lw=2)
    plt.title('Y vs. Y_noise (alpha='+str(a)+')')
    
    f, Pxx_den = scipy.signal.periodogram(y_noise)

    #estimate the model parameters using the Yule-Walker method 
    rho, sigma = sm.regression.yule_walker(y_noise, order=6, method='mle')
    
    a_est = np.append(1,-rho)
    
    w, h = scipy.signal.freqz(sigma**2, a_est)
    #plot
    plt.figure()
    plt.plot(f[1:], 10*np.log10((np.abs(Pxx_den[1:]))), )
    plt.plot(w/(2*np.pi), 20*np.log10((np.abs(h))), label='AR (6)', lw=4, color='tab:red')
    plt.xlabel(r'Normalized Frequency')
    plt.ylabel(r'Power/frequency')
    plt.title(r'Spectral Density Estimate (alpha='+str(a)+')')
    plt.legend()
    
    
"""Question 2"""
import wave
import numpy as np 
import matplotlib.pyplot as plt
import IPython.display as ipd
from scipy.signal import welch, bessel, filtfilt, stft, spectrogram

"""Had"""
#######################
audio_had = wave.open('Assignment 10 audio(had).wav','r')
number_samples_had = audio_had.getnframes() #number of samples in file
rate_had = audio_had.getframerate() # sampling rate (in Hz)
data_had = np.frombuffer(audio_had.readframes(number_samples_had), dtype=np.int32) #data as a numpy array
data_had = data_had[0:len(data_had)]
time_had=np.arange(0,(number_samples_had-1)*(1/rate_had),(1/rate_had)) # time vector as a numpy array
audio_had.close()    



"""Plotting Original Audio Signal"""
plt.figure()
plt.plot(data_had)
plt.ylabel('Amplitude')
plt.title('Audio Signal (had)')


"""Finding Power Spectrum"""
plt.figure()
plt.title('Had Spectrum')
plt.specgram(data_had, Fs=rate_had)
plt.xlabel('Time')
plt.ylabel('Frequency')

"""Hood"""
#######################
audio_hood=wave.open('Assignment 10 audio(hood).wav','r')
number_samples_hood=audio_hood.getnframes() #number of samples in file
rate_hood=audio_hood.getframerate() # sampling rate (in Hz)
data_hood=np.frombuffer(audio_hood.readframes(number_samples_hood), dtype=np.int32) #data as a numpy array
time_hood=np.arange(0,(number_samples_hood-1)*(1/rate_hood),(1/rate_hood)) # time vector as a numpy array
audio_hood.close()    



"""Plotting Original Audio Signal"""
plt.figure()
plt.plot(data_hood)
plt.ylabel('Amplitude')
plt.title('Audio Signal (hood)')


"""Finding Power Spectrum"""
plt.figure()
plt.title('Hood Spectrum')
plt.specgram(data_hood, Fs=rate_hood)
plt.xlabel('Time')
plt.ylabel('Frequency')


"""Heed"""    
#######################
audio_heed=wave.open('Assignment 10 audio(heed).wav','r')
number_samples_heed=audio_heed.getnframes() #number of samples in file
rate_heed=audio_heed.getframerate() # sampling rate (in Hz)
data_heed=np.frombuffer(audio_heed.readframes(number_samples_heed), dtype=np.int32) #data as a numpy array
time_heed=np.arange(0,(number_samples_heed-1)*(1/rate_heed),(1/rate_heed)) # time vector as a numpy array
audio_heed.close()    


"""Plotting Original Audio Signal"""
plt.figure()
plt.plot(data_heed)
plt.ylabel('Amplitude')
plt.title('Audio Signal (heed)')


"""Finding Power Spectrum"""
plt.figure()
plt.title('Heed Spectrum')
plt.specgram(data_heed, Fs=rate_heed)
plt.xlabel('Time')
plt.ylabel('Frequency')
