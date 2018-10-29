# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 02:52:14 2018

@author: Ahmad
"""

#!/usr/bin/python

import random
import numpy
import matplotlib.pyplot as plt
import pickle

from outlier_cleaner import outlierCleaner


### load up some practice data with outliers in it
ages = pickle.load( open("practice_outliers_ages.pkl", "r") )
net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "r") )

## Ahmad just to know it is list type here
#print net_worths
#print "BEFORE: ",type(net_worths)
#----------------------------------------------
### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

## Ahamd just to know it has been converted from list to numpy array here
#print net_worths
#print "AFTER:  ",type(net_worths)
#print net_worths.shape
#print net_worths.dtype


from sklearn.cross_validation import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(ages_train, net_worths_train)








"""
############  This is the exact instruction from the lesson 8 quiz number 10 ############
## Deploy a linear regression, where net worth is the target and the feature being used to predict it is 
# a person’s age (remember to train on the training data!).
"""


try:
    plt.plot(ages, reg.predict(ages), color="blue")
    #plt.plot(ages_test, reg.predict(ages_test), color="blue")
except NameError:
    pass

#print "score on whole data = ", reg.score(ages , net_worths)
    

##  what slope does your regression have? lesson 8 quiz number 10
#print "slope for all data = ", reg.coef_

## lesson 8 quiz number 11 
## What is the score you get when using your regression to make predictions with the test data?
#reg.fit(ages_train, net_worths_train)
#pred_test = reg.predict(ages_test)
#print "score on test data = ", reg.score(ages_test , net_worths_test)

plt.scatter(ages, net_worths)
plt.show()


### identify and remove the most outlier-y points
cleaned_data = []
print "111111111: ",len(cleaned_data)
try:
    predictions = reg.predict(ages_train)
    cleaned_data = outlierCleaner( predictions, ages_train, net_worths_train )
except NameError:
    print "your regression object doesn't exist, or isn't name reg"
    print "can't make predictions to use in identifying outliers"



print "222222222: ",len(cleaned_data)
print cleaned_data
 





### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)   
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    ### refit your cleaned data!
    try:
        reg.fit(ages, net_worths)
        plt.plot(ages, reg.predict(ages), color="blue")
    except NameError:
        print "you don't seem to have regression imported/created,"
        print "   or else your regression object isn't named reg"
        print "   either way, only draw the scatter plot of the cleaned data"
    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()
    print "333333333: ",len(cleaned_data)
    print "444444444: ",len(ages) + len(net_worths)
    print "555555555: ",len(net_worths)
    print "666666666: ",max(errors)
    print "errors type: : ",type(errors)
    print cleaned_data[89][1]
    
 
        
      




else:
    print "outlierCleaner() is returning an empty list, no refitting to be done"

