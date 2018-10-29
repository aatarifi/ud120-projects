#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

'''
# Ahmad just AdaBoost
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=100)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "accuracy: ", clf.score(features_test, labels_test)

'''

# Ahmad many classifiers at once
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


clf1 = AdaBoostClassifier(n_estimators=100)
clf2 = RandomForestClassifier(random_state=1)
clf3 = KNeighborsClassifier(n_neighbors=7)
clf4 = GaussianNB()
clf5 = SVC(kernel='rbf', probability=True)
clf6 = DecisionTreeClassifier(max_depth=4)

eclf = VotingClassifier(estimators=[('adb', clf1), ('rf', clf2), ('kn', clf3), ('gnb',clf4), ('svc',clf5), ('dt',clf6)], voting='hard')

eclf = eclf.fit(features_train, labels_train)
pred = eclf.predict(features_test)

print "\n\n\n\n"

for clf, label in zip([clf1, clf2, clf3, clf4, clf5, clf6, eclf], ['AdaBoost', 'Random Forest','KNeighbors', 'Naive Bayes','SVC','DecisionTree', 'Ensemble']):
   scores = cross_val_score(clf, features_test, labels_test , cv=8, scoring='accuracy')
   print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))
   
print "\n\n\n\n"   
   
   
   

    
try:
    
    prettyPicture(eclf, features_test, labels_test)
    
    
except NameError:
    pass 
    
    


eclf_1 = VotingClassifier(estimators=[('adb', clf1), ('rf', clf2), ('kn', clf3), ('gnb',clf4), ('svc',clf5), ('dt',clf6)], voting='soft')

eclf_1 = eclf_1.fit(features_train, labels_train)
pred_1 = eclf_1.predict(features_test)

print "\n\n\n\n"

for clf, label in zip([clf1, clf2, clf3, clf4, clf5, clf6, eclf_1], ['AdaBoost', 'Random Forest','KNeighbors', 'Naive Bayes','SVC','DecisionTree', 'Ensemble']):
   scores = cross_val_score(clf, features_test, labels_test , cv=8, scoring='accuracy')
   print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))
   
   
print "\n\n\n\n"   
   
try:
    
    prettyPicture(eclf_1, features_test, labels_test)
    
except NameError:
    pass   

'''
clf1.fit(features_train, labels_train)
clf2.fit(features_train, labels_train)
clf3.fit(features_train, labels_train)
clf4.fit(features_train, labels_train)
clf5.fit(features_train, labels_train)
clf6.fit(features_train, labels_train)

eclf.fit(features_train, labels_train)

pred1 = clf1.predict(features_test)
pred2 = clf2.predict(features_test)
pred3 = clf3.predict(features_test)
pred4 = clf4.predict(features_test)
pred5 = clf5.predict(features_test)
pred6 = clf6.predict(features_test)

pred7 = eclf.predict(features_test)





for clf, label in zip([clf1, clf2, clf3, clf4, clf5, clf6, eclf], ['AdaBoost', 'Random Forest','KNeighbors', 'Naive Bayes','SVC','DecisionTree', 'Ensemble']):
   scores = cross_val_score(clf, features_test, labels_test , cv=8, scoring='accuracy')
   print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))




try:
    prettyPicture(eclf, features_test, labels_test)
    
except NameError:
    pass

try:
    prettyPicture(eclf_1, features_test, labels_test)
    
except NameError:
    pass
'''