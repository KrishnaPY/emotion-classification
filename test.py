import matplotlib.pyplot as plt  
import numpy as np   
import csv
from sklearn.preprocessing import StandardScaler

cry = np.genfromtxt("adult_cry_extract40.csv", delimiter=',', skip_header=True)
laugh = np.genfromtxt("adult_laugh_extract40.csv", delimiter=',', skip_header=True)

#print cry[30,:], laugh[30,:]

scaler = StandardScaler() # normalizing the data to unit variance
cry[:,1:] = scaler.fit_transform(cry[:,1:])
laugh[:,1:] = scaler.fit_transform(laugh[:,1:])
print cry[5:7,:], laugh[5:7,:]

cry_mfcc = cry[:,3:]
laugh_mfcc = laugh[:,3:]

cry_mfcc_avg = np.average(cry[:,3:],axis=1)
laugh_mfcc_avg = np.average(laugh[:,3:],axis=1)
cry_mfcc_avg[np.abs(cry_mfcc_avg)>80] = 0
laugh_mfcc_avg[np.abs(laugh_mfcc_avg)>80] = 0


cry_flux = cry[:,2]
laugh_flux = laugh[:,2]
cry_flux[np.abs(cry_flux)>80] = 0
laugh_flux[np.abs(laugh_flux)>80] = 0

cry_cent = cry[:,1]
laugh_cent = laugh[:,1]

fig = plt.figure()

plt.scatter(cry_mfcc[:,10],cry_cent,c='r',label='cry')
plt.scatter(laugh_mfcc[:,10],laugh_cent,c='b',label='laugh')

plt.xlabel('mfcc ')
plt.ylabel('flux')

plt.show()