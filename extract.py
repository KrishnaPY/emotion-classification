import numpy as np
import scipy.io.wavfile
from dft import spectral_centroid, spectral_flux, pitch
import os
import cmath
import math
import timeit	
import librosa.feature
import csv

csvfile = "laugh1.csv"
featureRow = ['emotion','centroid','flux','pitch','mfcc']

directory = '/home/krispy/Desktop/DSP Project/oxvoc_dataset/Adult_laugh_sounds'
frame_time = 30
samples_per_frame = 1024
centroid_list = []
flux_list = []
pitch_list = []
x_old = np.zeros((1,samples_per_frame))
x_old2 = np.zeros((1,samples_per_frame))
k=1
x = np.random.random((1,samples_per_frame))

with open(csvfile, "a") as fp:
	wr = csv.writer(fp, dialect='excel')
	#wr.writerow(featureRow)
	for filename in os.listdir(directory):
		if filename.endswith('.wav') and k<2:		
			print os.path.join(directory,filename)
			rate ,data = scipy.io.wavfile.read(os.path.join(directory,filename), mmap= False)
			N = int(np.size(data)/samples_per_frame)
		    	for i in range(N-1):
		    		x[0,:] = data[i*samples_per_frame:(i+1)*samples_per_frame]
		    		centroid = spectral_centroid(x,rate)
				flux = spectral_flux(x,x_old)
				pitch_freq = pitch(x,rate)
				coeffs = np.average((librosa.feature.mfcc(x[0,:],sr=rate)),axis=1)
				np.append(['cry',centroid],coeffs,axis=1)
				wr.writerow(['cry',centroid, flux, coeffs[0],coeffs[1],coeffs[2],coeffs[3],coeffs[4],coeffs[5],coeffs[6],coeffs[7],coeffs[8],coeffs[9],coeffs[10],coeffs[11],coeffs[12],coeffs[13],coeffs[14],coeffs[15],coeffs[16],coeffs[17],coeffs[18],coeffs[19]])
				'''
				centroid_list.append(centroid)
				flux_list.append(flux)
				pitch_list.append(pitch_freq)
				x_old2 = x_old
				'''
				x_old = x
				
			k = k+1
		else:
			continue
	








    
