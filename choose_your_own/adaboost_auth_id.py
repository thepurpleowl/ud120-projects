# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:08:05 2016

@author: surya
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.ensemble import AdaBoostClassifier
clf=AdaBoostClassifier(n_estimators=50,random_state=None)

t0= time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t1= time()
pred=clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(labels_test,pred)
print accuracy