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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "data points (people) in the dataset: ", \
        len(enron_data)

print "For each person,features available: ", \
        len(enron_data[enron_data.keys()[0]].keys())

count_poi=0
for k in enron_data:
    if enron_data[k]["poi"]==1:
        count_poi +=1   
        
print "POIs in the E+F dataset: ", count_poi

i=0
with open("../final_project/poi_names.txt", "r") as f:
    for i,l in enumerate(f):
        i +=1
print "POIse in the POI text file: ", (i-2)#for first two unnecessary lines

#to check features of each name
'''for i,l in enumerate(enron_data[enron_data.keys()[0]].keys()):
    print (enron_data[enron_data.keys()[0]].keys())[i]'''
    
print "The stock belonging to James Prentice: ",enron_data['PRENTICE JAMES']['total_stock_value']

print "email messages from Wesley Colwell to poi:",enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "value of stock options exercised by Jeffrey Skilling: ", \
            enron_data['SKILLING JEFFREY K']['exercised_stock_options']
    
quantified_salary_count = 0
poi_salary_count = 0
for k in enron_data:
    if enron_data[k]['salary'] != 'NaN':
        quantified_salary_count += 1
for k in enron_data:
    if (enron_data[k]['salary'] != 'NaN') & (enron_data[k]['poi']):
        poi_salary_count += 1
print "folks in having a quantified salary: ",quantified_salary_count
print "folks in having NAN as salary: ",\
        float(len(enron_data)-quantified_salary_count)/len(enron_data)
print "folks in having NAN as salary: ",\
        float(poi_salary_count)/len(enron_data)