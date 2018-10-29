#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 

### Lesson 14_18 what's the accuracy with a testing regime properly deployed?
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train )

## Lesson 15_28 How many POIs are predicted for the test set for your POI identifier?

pred = clf.predict(features_test)
print len([e for e in pred if e == 1.0])
#sum(pred)

## Lesson 15_29 How many people total are in your test set?
print len(pred)

## Lesson 15_31 Look at the predictions of your model and compare them to the true test labels. 
## Do you get any true positives? (In this case, we define a true positive as a case where both 
##                                the actual label and the predicted label are 1)
print pred
print "\n\n"
print labels_test

print clf.score(features_test, labels_test)

from sklearn.metrics import confusion_matrix, precision_score, recall_score, classification_report

## Lesson 15_32 What's the precision of your POI identifier
print "precision: ",precision_score(labels_test, pred)

## Lesson 15_33 What's the recall of your POI identifier
print "recall: ", recall_score(labels_test, pred)

## Lesson 15_38_39
# Here are some made-up predictions and true labels for a hypothetical test set; 
# fill in the following boxes to practice identifying true positives, false positives, true negatives, and false negatives. 
# Let’s use the convention that “1” signifies a positive result, and “0” a negative. 
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

# What's the precision of this classifier?
precision_score(true_labels, predictions)

# What's the recall of this classifier?
recall_score(true_labels, predictions)


## confusion_matrix 
cm = confusion_matrix(true_labels, predictions)

print cm, '\n'
print '{0} True positives'.format(cm[1][1])
print '{0} True negatives'.format(cm[0][0])
print '{0} False positives'.format(cm[0][1])
print '{0} False negatives'.format(cm[1][0])







































































