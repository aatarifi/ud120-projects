#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
#from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

# time to train the classifier 
t0 = time()

clf.fit(features_train,labels_train)

print "training time:", round(time()-t0, 3), "s"


# time to make predictions with the trained classifier
t0 = time()

pred= clf.predict(features_test)

print "predicting time:", round(time()-t0, 3), "s"

print clf.score(features_test,labels_test)

#########################################################

