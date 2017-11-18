import librosa
import librosa.display
import scipy
import matplotlib.pyplot as plt
import numpy as np
frame_time = 30
overlap = 0
rate ,data = scipy.io.wavfile.read('Adult_laugh_sounds/Adultfemale_laugh0'+str(5)+'.wav',mmap= False)
#data2,sr =  librosa.core.load(path='Adult_cry_sounds/Adultfemale_cry02.wav',sr=None)
'''
filename = librosa.util.example_audio_file()
y, sr = librosa.load(filename)
print sr, y[11000:11100]
'''

plt.figure()
plt.plot(librosa.stft(data,n_fft = 1024, hop_length = 1024))

plt.show()
#D = librosa.amplitude_to_db(librosa.stft(data), ref=np.max)

'''
plt.figure()
librosa.display.specshow(D, y_axis='linear')
plt.show()
'''
'''
frame_length = int(rate*0.001*frame_time)
num_frames = int(data.size /frame_length)
intervals = [ [i*frame_length + 1, (i+1)*frame_length] for i in range(num_frames) ]
'''



'''
print rate, data.size, np.amin(data), np.amax(data)

plt.plot(np.fft.fft(data))
plt.show()
print librosa.core.zero_crossings(data, np.mean(data))
'''
