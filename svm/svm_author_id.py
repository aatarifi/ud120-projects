# coding: utf-8
# !/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='rbf', C=10000.0)

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

print len(features_train)
print len(labels_train)
t0 = time()
clf.fit(features_train, labels_train)
print "training time", round(time() - t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)

print "predicting time", round(time() - t0, 3), "s"

# print "The prediction for element 10 of the test set is: ", pred[0]
# print "The prediction for element 26 of the test set is: ", pred[26]
# print "The prediction for element 50 of the test set is: ", pred[50]

# Ahmad added
type(pred)


# Ahmad added the following code to answer lesson 3 question 37
def counter():
    chris = 0
    sara = 0
    i = 0
    for i in np.nditer(pred):
        if i == 1:
            chris += 1
        if i == 0:
            sara += 1

            # print "prediction to be in the “Chris” (1) =  ",chris
    # print "prediction to be in the “Sara” (0) =  ",sara
    # return chris, sara
    return chris, sara


print "prediction to be in the “Chris” (1) and “Sara” (0) is:   ", counter()

print accuracy_score(pred, labels_test)

#########################################################
