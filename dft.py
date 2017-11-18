import numpy as np  
import os
import cmath
import math
import timeit	

directory = '/home/krispy/Desktop/DSP Project/oxvoc_dataset/Adult_cry_sounds'
'''
for filename in os.listdir(directory):
	if filename.endswith('.wav'):
		print os.path.join(directory,filename)
	else:
		continue
'''


def DFT(x): 
	x = np.asarray(x,dtype = float)
	N = x.shape[1]
	n = np.arange(N)
	M = np.exp(-2j*np.pi*np.outer(n,n)/N)
	return np.dot(x,M)


def FFT(x):
	x = np.asarray(x, dtype = float)
	N = x.shape[1]
	if N<32:
		return DFT(x)
	else:
		if  np.log2(N)%1 > 0:
			x = np.append(x,
					np.zeros((1,int(pow(2,np.ceil(np.log(N)/np.log(2))))-N)),axis =1)
			N = x.shape[1]
		X_even = FFT(x[:,::2])
        X_odd = FFT(x[:,1::2])
        factor = np.exp(-2j * np.pi * np.arange(N/2) / N)
        return np.append(X_even + factor * X_odd,
                               X_even - factor * X_odd, axis = 1)

def fft_freqs(x, rate):
	N = x.shape[1]
	p1 = np.arange(0,(N-1)//2 +1) # adf
	p2 = np.arange(-(N//2),0)#df
	freqs = np.append(p1,p2)#dfa
	return freqs * rate / N

def spectral_centroid(x, rate):
	N = x.shape[1]
	magnitudes = np.abs(FFT(x))[:,:N//2 +1]
	freqs = fft_freqs(x, rate)[:N//2 +1]
	print magnitudes.shape, freqs.shape
	return np.sum(magnitudes*freqs)/np.sum(magnitudes)# return weighted mean

def spectral_flux(x1, x2): # input is in time domain NEED TO pass FFT to opt
	return np.sum(np.abs(FFT(x1)-FFT(x2))**2)
	
def hamming(n):
	return 0.54-0.46*np.cos(2*np.pi*np.arange(n)/n)

def cepstrum(x): # input is in time NEED TO pass FFT to opt
	return np.fft.ifft(np.log(np.abs(FFT(x))))
	



x = np.random.random((1,32))
y = np.random.random((1,1024))
start = timeit.default_timer()

print cepstrum(x)

stop = timeit.default_timer()

print stop - start 






	