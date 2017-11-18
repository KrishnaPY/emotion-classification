import numpy as np
import matplotlib as plt
import scipy
import dft

import pickle
'''
# obj0, obj1, obj2 are created here...


# Getting back the objects:
with open('objs.pkl') as f:  # Python 3: open(..., 'rb')
    obj0, obj1, obj2 = pickle.load(f)
'''

directory = '/home/krispy/Desktop/DSP Project/oxvoc_dataset/Adult_cry_sounds'

frame_time = 30
samples_per_frame = 1024
centroid_list = []
flux_list = []
pitch_list = []
k=1
for filename in os.listdir(directory):
	if filename.endswith('.wav') and k < 2:
		x_old = np.zeros((1,samples_per_frame))
		print os.path.join(directory,filename)
	    rate ,data = scipy.io.wavfile.read(filename, mmap= False)
		N = int(np.size(data)/samples_per_frame)
		for i in range(N):
			x = data[i*samples_per_frame:(i+1)*samples_per_frame]
			centroid = spectral_centroid(x,rate)
			flux = spectral_flux(x,x_old)
			pitch_freq = pitch(x,rate)
			centroid_list.append(centroid)
			flux_list.append(flux)
			pitch_list.append(pitch_freq)
			x_old = x
		k = k+1
	else:
		continue

with open('cry_features.pkl', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([centroid_list, flux_list, pitch_list], f)








    