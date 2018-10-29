#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

popped_element = data_dict.pop("TOTAL", 0 )
print('The popped element is:', popped_element)
#print('The data_dict is:', data_dict)
data = featureFormat(data_dict, features)

"""
Ahmad comments test
"""
#print data
#print type(data)
#print len(data)
#print data[1][0]
#print data.shape


### your code below
# Lesson 8_14 Enron Outliers

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

"""
Lesson 8_15
Identify the Biggest Enron Outlier
What’s the name of the dictionary key of this data point?
"""
## Person ID:  TOTAL 
## salary:  26704229     just by Ctrl+F  you can find the name which is TOTAL
def getMaxSalary():
    allSalaries = []
    for ed_id, ed_info in data_dict.iteritems():
        print"\nPerson ID: ", ed_id, "\nsalary: ",ed_info["salary"]
        
        allSalaries.append(float(ed_info["salary"]))
    return   "The Biggest Enron Outlier: ",max(allSalaries)


print getMaxSalary()



"""
Lesson 8_18
We would argue that there’s 4 more outliers to investigate; let's look at a couple of them. 
Two people made bonuses of at least 5 million dollars, and a salary of over 1 million dollars; 
in other words, they made out like bandits. What are the names associated with those points?
"""

def getBanditsNames():
  for i,j in data_dict.iteritems():
    if j["salary"] > 1000000 and j["bonus"] > 5000000:
        if j["salary"] != 'NaN' and j["bonus"] != 'NaN':
           print "\nName: ",i
           print "Salary: ",j["salary"] ," ", "\nBonus: ",j["bonus"]
    
       
print "\n\nBANDITS: ",getBanditsNames()



"""
Or another way of doing the same but not sure if logically correct as these two points are features Ahmad
# Lesson 8_14 Enron Outliers and 8_15

"""

target , features = targetFeatureSplit( data )

## Person ID:  TOTAL 
## salary:  26704229     just by Ctrl+F  you can find the name which is TOTAL
print "The Biggest Enron Outlier: ",max(target)


#print target
#print "___________________________________________"
#print features
#
#print type(target)
#print type(features)

for x,y in zip(target,features):
    matplotlib.pyplot.scatter( x, y )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

     

