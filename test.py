import matplotlib.pyplot as plt  
import numpy as np   
import csv
from sklearn.preprocessing import StandardScaler

cry = np.genfromtxt("ACry_extract40.csv", delimiter=',', skip_header=True)
laugh = np.genfromtxt("ALaugh_extract40.csv", delimiter=',', skip_header=True)

#print cry[30,:], laugh[30,:]

scaler = StandardScaler() # normalizing the data to unit variance
cry[:,1:] = scaler.fit_transform(cry[:,1:])
laugh[:,1:] = scaler.fit_transform(laugh[:,1:])
print cry[5:7,:], laugh[5:7,:]

cry_mfcc = cry[:,5:]
laugh_mfcc = laugh[:,5:]

cry_mfcc_avg = np.average(cry[:,5:],axis=1)
laugh_mfcc_avg = np.average(laugh[:,5:],axis=1)
cry_mfcc_avg[np.abs(cry_mfcc_avg)>80] = 0
laugh_mfcc_avg[np.abs(laugh_mfcc_avg)>80] = 0


cry_spread = cry[:,2]
laugh_spread = laugh[:,2]
cry_spread[np.abs(cry_spread)>80] = 0
laugh_spread[np.abs(laugh_spread)>80] = 0

cry_cent = cry[:,1]
laugh_cent = laugh[:,1]

cry_entropy = cry[:,3]
laugh_entropy = laugh[:,3]
cry_entropy[np.abs(cry_entropy)>80] = 0
laugh_entropy[np.abs(laugh_entropy)>80] = 0

cry_energy = cry[:,4]
laugh_energy = laugh[:,4]
cry_energy[np.abs(cry_energy)>80] = 0
laugh_energy[np.abs(laugh_energy)>80] = 0

fig = plt.figure()

#plt.scatter(cry_mfcc[:,10],cry_cent,c='r',label='cry')
#plt.scatter(laugh_mfcc[:,10],laugh_cent,c='b',label='laugh')

cry_scatter = plt.scatter(cry_entropy, cry_energy, marker = 'o', c='r',label='cry')
laugh_scatter = plt.scatter(laugh_entropy, laugh_energy, marker = 'x', c='b',label='laugh')
plt.legend((cry_scatter, laugh_scatter), ('Cry', 'Laugh'), scatterpoints = 1, loc = 'upper right', ncol = 2, fontsize = 10)

plt.xlabel('Entropy')
plt.ylabel('Energy')

plt.show()