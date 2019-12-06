# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:26:06 2019

@author: Edwin
"""

import numpy as np
import func.microdoppler_visualizer as mv
import mmwave.dsp as dsp
import scipy.io as sio
import matplotlib.pyplot as plt
    
#testDataCarNoise = sio.loadmat('data/mathworks/testDataCarNoise')
#trainDataCarNoise = sio.loadmat('data/mathworks/trainDataCarNoise')
#trainDataNoCar = sio.loadmat('data/mathworks/trainDataCarNoise')
plt.close('all')
load_data_flag = True

# =============================================================================
# Load data
# =============================================================================
data = []
sets = 2
setSize = 1000
if load_data_flag:
    print("[NOTE] ---------- Loading Data ----------")
    for i in range(sets):
        testDataNoCar = sio.loadmat('data/mathworks/test/testDataNoCar_'+str(i+1)+'.mat')
        data.append(testDataNoCar[list(testDataNoCar.keys())[-1]].squeeze())
        print("[NOTE] Loaded data subset ", i)
         
    print("[NOTE] Loading Labels")
    testLabelNoCar = sio.loadmat('data/mathworks/test/testLabelNoCar.mat')
    testLabelNoCar = testLabelNoCar[list(testLabelNoCar.keys())[-1]].squeeze()
    print("[NOTE] Label Loading Complete")
    
    print("[NOTE] Loading Time & Frequency Data")
    TF = sio.loadmat('data/mathworks/TF.mat')
    T = TF[list(TF.keys())[-1]].squeeze()
    F = TF[list(TF.keys())[-2]].squeeze()
    print("[NOTE] T F Loading Complete")

    data = np.array(data).transpose(0,3,1,2).reshape((sets*setSize,400,144))
   
    print("[NOTE] ---------- Data Loading Complete ----------")

# Check to see the data
#mv.classification_data_visualizer(data,label=testLabelNoCar)

# Grab only Single Pedestrian data
indices = np.where(testLabelNoCar == np.str_('ped    '))[0]     # Get all indices
trainDataPed = data[indices[indices<sets*setSize]]              # Only keep indices within subset of chosen data
trainLabelPed = testLabelNoCar[indices[indices<sets*setSize]]

# Grab only Single Bike data
indices = np.where(testLabelNoCar == np.str_('bic    '))[0]     # Get all indices
trainDataBic = data[indices[indices<sets*setSize]]              # Only keep indices within subset of chosen data
trainLabelBic = testLabelNoCar[indices[indices<sets*setSize]]

# Check to see the data
mv.classification_data_visualizer(trainDataBic, trainLabelBic)


# Gaussian Mixture Model
# PCA Feature Extraction


# Hidden Markov Model -- Lecture 13, Slide 39

