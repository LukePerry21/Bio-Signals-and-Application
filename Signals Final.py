# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:33:11 2021

@author: dmdur
"""

import numpy as np
import os 
from pathlib import Path
import pandas as pd 
import matplotlib.pyplot as plt
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15,5), 
          'axes.labelsize': 'x-large',
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 'x-large',
          'ytick.labelsize':'x-large'}
plt.rcParams.update(params)

"""Importing Data"""
###################################################

#Subject 1 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/01/1_raw_data_13-12_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

Data = data #Creating a large data set to story all data

#Subject 1 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/01/2_raw_data_13-13_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 2 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/02/1_raw_data_14-19_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 2 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/02/2_raw_data_14-21_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 3 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/03/1_raw_data_09-32_11.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 3 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/03/2_raw_data_09-34_11.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 4 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/04/1_raw_data_18-02_24.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 4 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/04/2_raw_data_18-03_24.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 5 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/05/1_raw_data_10-28_30.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 5 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/05/2_raw_data_10-29_30.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 6 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/06/1_raw_data_10-38_11.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 6 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/06/2_raw_data_10-40_11.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 7 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/07/1_raw_data_18-48_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 7 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/07/2_raw_data_18-50_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 8 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/08/1_raw_data_12-14_23.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 8 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/08/2_raw_data_12-16_23.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 9 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/09/1_raw_data_12-41_23.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 9 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/09/2_raw_data_12-43_23.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 10 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/10/1_raw_data_11-08_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 10 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/10/2_raw_data_11-10_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 11 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/11/1_raw_data_13-11_18.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 11 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/11/2_raw_data_13-13_18.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 12 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/12/1_raw_data_11-35_28.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 12 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/12/2_raw_data_11-36_28.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 13 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/13/1_raw_data_13-26_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 13 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/13/2_raw_data_13-29_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 14 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/14/1_raw_data_09-50_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 14 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/14/2_raw_data_09-51_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 15 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/15/1_raw_data_08-49_13.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 15 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/15/2_raw_data_08-51_13.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 16 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/16/1_raw_data_12-12_25.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 16 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/16/2_raw_data_12-14_25.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 17 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/17/1_raw_data_11-19_23.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 17 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/17/2_raw_data_11-20_23.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 18 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/18/1_raw_data_12-35_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 18 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/18/2_raw_data_12-37_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 19 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/19/1_raw_data_12-10_26.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 19 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/19/2_raw_data_12-11_26.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 20 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/20/1_raw_data_11-41_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 20 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/20/2_raw_data_11-43_22.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 21 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/21/1_raw_data_20-28_24.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 21 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/21/2_raw_data_20-30_24.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 22 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/22/1_raw_data_12-37_28.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 22 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/22/2_raw_data_12-39_28.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 23 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/23/1_raw_data_13-18_05.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 23 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/23/2_raw_data_13-19_05.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 24 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/24/1_raw_data_10-16_12.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 24 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/24/2_raw_data_10-17_12.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 25 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/25/1_raw_data_14-51_24.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 25 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/25/2_raw_data_14-53_24.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 26 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/26/1_raw_data_10-22_29.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 26 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/26/2_raw_data_10-23_29.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 27 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/27/1_raw_data_12-19_06.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 27 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/27/2_raw_data_12-20_06.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 28 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/28/1_raw_data_12-10_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 28 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/28/2_raw_data_12-11_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 29 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/29/1_raw_data_10-17_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 29 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/29/2_raw_data_10-18_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 30 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/30/1_raw_data_09-49_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 30 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/30/2_raw_data_09-50_21.03.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 31 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/31/1_raw_data_11-15_11.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 31 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/31/2_raw_data_11-16_11.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 32 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/32/1_raw_data_12-04_27.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 32 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/32/2_raw_data_12-06_27.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 33 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/33/1_raw_data_09-49_12.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 33 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/33/2_raw_data_09-50_12.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 34 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/34/1_raw_data_10-51_07.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 34 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/34/2_raw_data_10-53_07.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 35 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/35/1_raw_data_10-03_13.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 1 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 35 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/35/2_raw_data_10-05_13.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 36 Trial 1
data = pd.read_csv('EMG_data_for_gestures-master/36/1_raw_data_13-03_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

#Subject 36 Trial 2
data = pd.read_csv('EMG_data_for_gestures-master/36/2_raw_data_13-04_15.04.16.txt', sep='\s+|\t+')#importing data
data.head()

#Creating subject label column
subject = np.arange(0,len(data))
subject[:] = 2 #specifying subject label
data['Subject'] = subject #adding subject label column

data_sets = [Data, data]
Data = pd.concat(data_sets)

###################################################
"""Test Plotting"""
###################################################
classes = list(['unmarked', 'hand at rest', 'hand clenched', 'wrist extension', 'radial deviations', 'ulnar deviations', 'extended palm'])

fig, ax = plt.subplots(figsize=(20,10))

time = data['time'].values * (1/2000)
channel = data['channel1'].values * (1000)
ax.plot(time, channel, label = classes[0], alpha = 0.10)
for i in data['class'].unique():
    if i > 0:
        time = data[data['class']==i]['time'].values * (1/2000)
        channel = data[data['class']==i]['channel1'].values * (1000)
        ax.plot(time, channel, '.', label = classes[i])
        
fig.legend();
ax.set_xlabel('Time (s)')
ax.set_ylabel('EMG (mV)')
ax.set_title('Channel 1')


###################################################
"""Feature Extraction"""
###################################################
Subjects_data = Data.groupby(['label','class'])
Subjects_data.head()