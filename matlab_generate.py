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

csvfile = 'cry_matlab.csv'

with open(csvfile,'a') as fp:
	wr = csv.writer(fp,dialect='excel')
	wr.writerows(cry)

csvfile = 'laugh_matlab.csv'

with open(csvfile,'a') as fp:
	wr = csv.writer(fp,dialect='excel')
	wr.writerows(laugh)
