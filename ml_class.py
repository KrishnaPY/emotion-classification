import matplotlib.pyplot as plt  
import numpy as np   
import csv
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder

percentTrain = 0.7
cry = np.genfromtxt("adult_cry_extract40.csv", delimiter=',', skip_header=True,dtype = ("|S10"))
laugh = np.genfromtxt("adult_laugh_extract40.csv", delimiter=',', skip_header=True, dtype =("|S10"))
print cry.shape
cry_train = cry[:int(percentTrain*cry.shape[0]),:]
cry_test = cry[int(percentTrain*cry.shape[0])+1:,:]

laugh_train = laugh[:int(percentTrain*laugh.shape[0]),:]
laugh_test = laugh[int(percentTrain*laugh.shape[0])+1:,:]

train = np.append(cry_train,laugh_train,axis =0)
test = np.append(cry_test,laugh_test,axis =0)

le = LabelEncoder()
Xtrain = train[:,1:]
Ytrain = train[:,0]
Ytrain = le.fit_transform(Ytrain)
Xtest = test[:,1:]
Ytest = test[:,0]
Ytest = le.fit_transform(Ytest)


print  Ytrain, le.fit_transform(Ytrain)

print Xtrain.shape, Xtest.shape




'''
rbf_kernel_svm_clf = Pipeline((("scaler",StandardScaler()),("svm_clf",SVC(kernel='rbf', gamma=5, C=0.001))))

rbf_kernel_svm_clf.fit(X,y)
'''