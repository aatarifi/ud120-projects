#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle



#with open("../final_project/final_project_dataset.pkl", "r") as f:
#    enron_data = pickle.load(f)

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


for ed_id, ed_info in enron_data.iteritems():
    print"\nPerson ID: ", ed_id
    
        
    for key in ed_info:
        print key + ':', ed_info[key]




"""
## print the entire main dictionary and the nested ones inside it
#print enron_data
 
## lenghth of main dictionary how many people are in it
print "len: ",len(enron_data)

## just a for loop to get the lenghth and names of the people are in it
j = 0
for i in enron_data:
    print i
    j += 1
    
    
print "j: ",j 

## loop through the nested dictionaries
for ed_id, ed_info in enron_data.items():
    print"\n Person ID:", ed_id
    
    for key in ed_info:
        print key + ':', ed_info[key]

"""

# The “poi” feature records whether the person is a person of interest, according to
# our definition. How many POIs are there in the E+F dataset?

i = 0
for ed_id, ed_info in enron_data.items():
    print"\n Person ID:", ed_id
    
    if ed_info['poi'] == True :
      print 'yes'
      i += 1

print "number of POI in the entire data: ",i  
         
## lenghth of one of the nested dictionary inside the main dictionary 
## For each person, how many features are available?
#print len(enron_data['METTS MARK'])


## What is the total value of the stock belonging to James Prentice?
print "PRENTICE JAMES total's value of stock: ",enron_data["PRENTICE JAMES"]["total_stock_value"]

## How many email messages do we have from Wesley Colwell to persons of interest?
print "COLWELL WESLEY email messages to poi: ",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

## What’s the value of stock options exercised by Jeffrey K Skilling?
print "Exrecised Stock Option by SKILLING JEFFREY K: ",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# # CFO Andrew Fastow, FASTOW ANDREW S
# # Chairman of directors Ken Lay   LAY KENNETH L
# # CEO SKILLING JEFFREY K

##Of these three individuals (Lay, Skilling and Fastow), who took home the most money 
##(largest value of “total_payments” feature)?
##How much money did that person get?
print "SKILLING JEFFREY K total money took home: ",enron_data["SKILLING JEFFREY K"]["total_payments"]
print "LAY KENNETH L total money took home: ",enron_data["LAY KENNETH L"]["total_payments"]
print "FASTOW ANDREW S total money took home: ",enron_data["FASTOW ANDREW S"]["total_payments"]
print "max: ", max(enron_data["SKILLING JEFFREY K"]["total_payments"], 
                   enron_data["LAY KENNETH L"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"] )




## How many folks in this dataset have a quantified salary? 
## What about a known email address?

counter = 0
valid_email = 0

counter += sum(enron_data[each]["salary"] !='NaN' for each in enron_data)
valid_email += sum(enron_data[each]["email_address"] !='NaN' for each in enron_data)





##############  OR
#counter += sum(each["salary"] !='NaN' for each in enron_data.itervalues())
#valid_email += sum(each["email_address"] !='NaN' for each in enron_data.itervalues())

print "Total quantified salaries: ",counter
print "Total valid email addresses: ",valid_email 
  


## How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? 
## What percentage of people in the dataset as a whole is this?
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp += 1
print "Total People have NaN for their total payment: ",count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())  

############# OR
total_payments = 0
total_payments += sum(enron_data[each]["total_payments"] =='NaN' for each in enron_data)
print "Total People have NaN for their total payment: ",total_payments

## How many POIs in the E+F dataset have “NaN” for their total payments? 
## What percentage of POI’s as a whole is this?
count_poi_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == 'True' :
        print
        count_poi_NaN_tp += 1
print "Total POI have NaN for their total payment: ",count_poi_NaN_tp
print float(count_poi_NaN_tp)/len(enron_data.keys())


## What is the total number of POI’s in the dataset  >> Ahmad  poi = True not False
count_poi = 0
for key in enron_data.keys():
    if enron_data[key]['poi'] == True :
        
        count_poi += 1
print "Total POI: ",count_poi


########   Good Answers for this entire exercise
"""
https://github.com/tuanavu/udacity-course/blob/master/intro_to_machine_learning/lesson/lesson_5_datasets_and_questions/explore_enron_data.py
"""
########


####  _____________Same code in different way___________________________________ ####
####  _____________Just add functions and another way of loading the file_______ ####

"""
import pickle

def ahmad_function1():

    with open("../final_project/final_project_dataset.pkl", "r") as f:
        enron_data = pickle.load(f)
    
    for ed_id, ed_info in enron_data.items():
        print"\nPerson ID: ", ed_id
        
        for key in ed_info:
            print key + ':', ed_info[key]



def ahmad_function2():

    with open("../final_project/final_project_dataset.pkl", "r") as f:
        enron_data = pickle.load(f)
    
    #enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    
    
    ## print the entire main dictionary and the nested ones inside it
    #print enron_data
     
    ## lenghth of main dictionary how many people are in it
    print "len: ",len(enron_data)
    
    ## just a for loop to get the lenghth and names of the people are in it
    j = 0
    for i in enron_data:
        print i
        j += 1
        
        
    print "j: ",j 
    
    ## loop through the nested dictionaries
    for ed_id, ed_info in enron_data.items():
        print"\n Person ID:", ed_id
        
        for key in ed_info:
            print key + ':', ed_info[key]
    
    
    
    # The “poi” feature records whether the person is a person of interest, according to
    # our definition. How many POIs are there in the E+F dataset?
    
    i = 0
    for ed_id, ed_info in enron_data.items():
        print"\n Person ID:", ed_id
        
        if ed_info['poi'] == True :
          print 'yes'
          i += 1
    
    print "number of POI in the entire data: ",i  
             
    ## lenghth of one of the nested dictionary inside the main dictionary 
    ## For each person, how many features are available?
    #print len(enron_data['METTS MARK'])
    
    
    ## What is the total value of the stock belonging to James Prentice?
    print "PRENTICE JAMES total's value of stock: ",enron_data["PRENTICE JAMES"]["total_stock_value"]
    
    ## How many email messages do we have from Wesley Colwell to persons of interest?
    print "COLWELL WESLEY email messages to poi: ",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
    
    ## What’s the value of stock options exercised by Jeffrey K Skilling?
    print "Exrecised Stock Option by SKILLING JEFFREY K: ",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
    
    # # CFO Andrew Fastow, FASTOW ANDREW S
    # # Chairman of directors Ken Lay   LAY KENNETH L
    # # CEO SKILLING JEFFREY K
    
    ##Of these three individuals (Lay, Skilling and Fastow), who took home the most money 
    ##(largest value of “total_payments” feature)?
    ##How much money did that person get?
    print "SKILLING JEFFREY K total money took home: ",enron_data["SKILLING JEFFREY K"]["total_payments"]
    print "LAY KENNETH L total money took home: ",enron_data["LAY KENNETH L"]["total_payments"]
    print "FASTOW ANDREW S total money took home: ",enron_data["FASTOW ANDREW S"]["total_payments"]
    print "max: ", max(enron_data["SKILLING JEFFREY K"]["total_payments"], 
                       enron_data["LAY KENNETH L"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"] )



            
ahmad_function1()
ahmad_function2()           
            
"""

        
        



     