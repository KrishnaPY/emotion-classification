import numpy as np
import scipy.io.wavfile
from dft import spectral_centroid, spectral_flux, spectral_spread, spectral_entropy, energy,zcr, spectral_skew, spectral_kurt
import os
import cmath
import math
import timeit	
import librosa.feature
import csv

csvfile = "adult_cry2.csv"
featureRow = ['emotion','centroid','spread','entropy','skew','kurt','mfcc']

directory = '/home/krispy/Desktop/DSP Project/oxvoc_dataset/Adult_cry_sounds'
frame_time = 40
samples_per_frame = 2048
centroid_list = []
flux_list = []
pitch_list = []
x_old = np.zeros((1,samples_per_frame))
x_old2 = np.zeros((1,samples_per_frame))

hop = 4

x = np.random.random((1,samples_per_frame))

with open(csvfile, "a") as fp:
	wr = csv.writer(fp, dialect='excel')
	#wr.writerow()
	wr.writerow(featureRow)
	for filename in os.listdir(directory):
		if filename.endswith('.wav'):		
			print os.path.join(directory,filename)
			rate ,data = scipy.io.wavfile.read(os.path.join(directory,filename), mmap= False)
			N = int(np.size(data)/samples_per_frame)
		    	for i in range(N-3):
		    		for j in range(hop):
			    		x[0,:] = data[i*samples_per_frame + int(j/hop)*samples_per_frame:(i+1)*samples_per_frame +int(j/hop)*samples_per_frame]
			    		centroid = spectral_centroid(x,rate)
			    		skew = spectral_skew(x,rate)
			    		kurt = spectral_kurt(x,rate)
					flux = spectral_flux(x,x_old)
					zc = zcr(x,rate)
					spread = spectral_spread(x, rate)
					entropy = spectral_entropy(x)
					ener = energy(x, rate)
					coeffs = np.average((librosa.feature.mfcc(x[0,:],sr=rate)),axis=1)
					
					wr.writerow(np.append([0,centroid,spread,entropy,skew,kurt],coeffs))
					#wr.writerow(['cry',centroid, flux, coeffs[0],coeffs[1],coeffs[2],coeffs[3],coeffs[4],coeffs[5],coeffs[6],coeffs[7],coeffs[8],coeffs[9],coeffs[10],coeffs[11],coeffs[12],coeffs[13],coeffs[14],coeffs[15],coeffs[16],coeffs[17],coeffs[18],coeffs[19]])
					'''

					centroid_list.append(centroid)
					flux_list.append(flux)
					pitch_list.append(pitch_freq)
					x_old2 = x_old
					'''
					x_old = x
				
		else:
			continue
	








    
