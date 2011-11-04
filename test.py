from dataload import getXy
from utility import sim_pearson, sim_cosine, euclidean, hamming, normalize, mae
import numpy as np
from knn import KNeighborRegressor, KNeighborClassifier
from evaluate import Evaluater
from itertools import product

#datafile = 'dataforest'
#X, y = getXy(datafile) # housing data
#X, y = getXy(datafile, delimiter=',')

#reg = KNeighborRegressor(X, y, 3, sim_cosine)
#e = Evaluater(reg, test_percentage = 5)
#print e.evaluate()
#del e, reg
#print "after normalization"
#normalize(X)


#reg = KNeighborRegressor(X, y, 5, sim_cosine, r_method="uniform")
#reg = KNeighborClassifier(X, y, 5, sim_pearson, r_method="uniform")

#e = Evaluater(reg, test_percentage = 10)
#print e.evaluate()

datafiles = ['dataspam']
k = [1,3,5,7,9]
metrics = [sim_cosine, sim_pearson, euclidean]
r_method = ['uniform', 'distance']
n = [True, False]
#percentage = [10, 20, 30]
#k = [5]
#percentage = [10]
prod = product(datafiles, k, metrics, r_method, n)
for filename, k, metric, r_m, n in prod:
    if filename == 'datahouse':
        X, y = getXy(filename)
    else:
        X, y = getXy(filename, delimiter=',')
    if n:
        normalize(X)
        print 'data is normalized'
    else:
        print 'data is not normalized'
    reg = KNeighborClassifier(X, y, k, metric, r_method=r_m)
    e = Evaluater(reg, test_percentage = 30)
    print '\t', e.evaluate()
    print '\n'




    



    #reg = KNeighborClassifier(X, y, m, sim_cosine, r_method="uniform")
    #e = Evaluater(reg, test_percentage = l)
    #print 'Test: k=%s, test/all_data=%s' % (m, l)
    #print "\t", e.evaluate()
    #del reg, e



