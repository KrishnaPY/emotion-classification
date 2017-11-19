import numpy as np   
import csv
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import cross_val_score


percentTrain = 0.7
cry = np.genfromtxt("ACry_extract40.csv", delimiter=',', skip_header=True,dtype = ("|S10"))
laugh = np.genfromtxt("ALaugh_extract40.csv", delimiter=',', skip_header=True, dtype =("|S10"))
print cry.shape

data = np.append(cry,laugh,axis=0)
data = shuffle(data,random_state=0) # randomized the frames
print data[15,:]

le = LabelEncoder()
le.fit(data[:,0])
print list(le.classes_)
data[:,0] = le.fit_transform(data[:,0])

train = data[:int(percentTrain*data.shape[0]),:]
test = data[int(percentTrain*cry.shape[0])+1:,:]


Xtrain = train[:,1:]
Ytrain = train[:,0]
Xtest = test[:,1:]
Ytest = test[:,0]
'''
rbf_kernel_svm_clf = Pipeline((("scaler",StandardScaler()),("svm_clf",SVC(kernel='rbf', gamma=5, C=0.001))))

scores = cross_val_score(rbf_kernel_svm_clf, Xtrain, Ytrain, cv=5)
print scores

#rbf_kernel_svm_clf.fit(X,y)
'''