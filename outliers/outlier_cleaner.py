#!/usr/bin/python


import numpy as np
"""
I imported all of the 3 lines below from outlier_removal_regression
to be able to test the code implemented in outlierCleaner function right over here
"""
#from outlier_removal_regression import predictions
#from outlier_removal_regression import ages_train
#from outlier_removal_regression import net_worths_train



def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    errors = (np.absolute(net_worths - predictions))
    ## OR
    #errors = net_worths - predictions
    #errors = (np.absolute(errors))
    # OR
    #errors = ((net_worths - predictions)**2)
    """ 
        # using zip() to Make an iterator that aggregates elements from each of the iterables.

    """
    zipped = [(age, net_worth, error) for age, net_worth, error in zip(ages, net_worths, errors)]
    
    """ 
    # using sort() to sort all 3 arrays inside the tuples by ascending order as errors array is the key
    # here if you want you can have:
    # reverse - If true, the sorted list is reversed (or sorted in Descending order)
    # key - function that serves as a key for the sort comparison
    # and by the way :
    #sort() method doesn't return any value. Rather, it changes the original list.
    #If you want the original list, use sorted() because sorted() makes a copy and doesnt change the original
    # I used lambda as a way of accessing the errors 
    # https://www.afternerd.com/blog/python-sort-list/#sort-tuples
    """
   
    zipped.sort(key=lambda x:x[2])
    
    """
    # using zip() again after sorting the 3 arrays inside the list of tuples with
    # (if error <= (np.percentile(errors, 90)))  to clean the outilers data
    # https://www.dummies.com/education/math/statistics/how-to-calculate-percentiles-in-statistics/
    """

    zipped = [(age, net_worth, error) for age, net_worth, error in zip(ages, net_worths, errors) if error <= (np.percentile(errors, 90))]

      
    """
    ## All here about more study and understading the python zip() , numpy, and thier type status
    ## along the coding jurney here
    #return errors," \n ",len(zipped)
    """

#    print "len(zipped)",len(zipped)
#    print "len(ages)",len(ages)
#    print "len(net_worths)",len(net_worths)
#    print "len(errors)",len(errors)
#    print "zipped type",type(zipped)
#    print "ages type",type(ages)
#    print "net_worths type",type(net_worths)
#    print "errors type",type(errors)
#    print "zipped[0] type",type(zipped[0])
    
    """
    ## here i used *zip to unzip but this is only to test the code here 
    other wise the outlierCleaner function should return list of tuples 
    that will be unzipped and handeled further from the caller in the
    outlier_removal_regression.py
    """
#    ages_unzipped, net_worths_unzipped, errors_unzipped = zip(*zipped)
   
#    print "len(ages_unzipped)",len(ages_unzipped)
#    
#    print "len(net_worths_unzipped)",len(net_worths_unzipped)
#    print "len(errors_unzipped)",len(errors_unzipped)
#    
#    print "ages_unzipped type",type(ages_unzipped)
#    print "net_worths_unzipped type",type(net_worths_unzipped)
#    print "errors_unzipped type",type(errors_unzipped)
#
#    print ages_unzipped
#    print "before type ages_unzipped[0] is: ",type(ages_unzipped[0])
    
    """
    ## here convert the unzipped groups(which they are numpy arrays wrapped by tuple) into a numpy array
    ## in other word un wrap them from tuple 
    ## and reshape them (len(ages_unzipped), 1)  rows columns
    """
#    ages_unzipped       = np.reshape( np.array(ages_unzipped), (len(ages_unzipped), 1))
#    net_worths_unzipped = np.reshape( np.array(net_worths_unzipped), (len(net_worths_unzipped), 1))
#    
#    print "ages_unzipped type",type(ages_unzipped)
#    print "net_worths_unzipped type",type(net_worths_unzipped)
    #print ages_unzipped[0]
    #print "after type ages_unzipped[0] is : ",type(ages_unzipped[0])
    
    
    cleaned_data = zipped
    


    return cleaned_data
#__________________________________________________________________________#
#__________________________________________________________________________#
    
#test = outlierCleaner(predictions, ages_train, net_worths_train)

#print "Ahmad This is from outiler file: \n",test