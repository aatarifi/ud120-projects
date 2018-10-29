#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature

""" 
Perform the regression of bonus against salary--what’s the score on the test data?

"""
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )


""" 
Perform the regression of bonus against long term incentive--what’s the score on the test data?

"""
#features_list = ["bonus", "long_term_incentive"]
#data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
#target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(feature_train, target_train)











### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_train[0], target_train[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass

"""
Sneak Peek: Outliers Break Regressions  Lesson 7 LAST Question number 46 
"""
#reg.fit(feature_test, target_test)
#plt.plot(feature_train, reg.predict(feature_train), color="b") 
#print "Question_46 the score =  ", reg.score(feature_train, target_train)


plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()

## Extract the slope (stored in the reg.coef_ attribute) and the intercept. What are the slope and intercept?
print "slope =  ",reg.coef_
print "intercept =  ",reg.intercept_

"""
Imagine you were a less savvy machine learner, and didn’t know to test on a holdout test set. Instead, 
you tested on the same data that you used to train, by comparing the regression predictions to the target 
values (i.e. bonuses) in the training data. What score do you find? You may not have an intuition yet 
for what a “good” score is; this score isn’t very good (but it could be a lot worse)
"""
#pred_training = reg.predict(feature_train)
#print "score on training data: ", reg.score(feature_train, target_train)

""" 
Now compute the score for your regression on the test data, like you know you should. 
What’s that score on the testing data? If you made the mistake of only assessing on the training data, 
would you overestimate or underestimate the performance of your regression?
"""
#pred_testing = reg.predict(feature_test)
#print "score on testing data: ", reg.score(feature_test, target_test)
