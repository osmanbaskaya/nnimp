#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from base import BaseEstimator
from utility import sim_pearson
from sys import stderr
from heapq import nlargest
from operator import itemgetter
#from collections import Counter

#TODO : Fix these distance and uniform comparison. Use abstract factory 

TOL = 0.000000001

class KNeighborRegressor(BaseEstimator):
    
    def __init__(self, X, y, k=3, sim_metric=sim_pearson, r_method='uniform'):

        super(KNeighborRegressor, self).__init__(X, y, k, sim_metric, r_method)
        print self
        
    def calculate_rating(self, n_list):

        # n_list : [item_index, distance]
        n = len(n_list)

        if self.r_method == 'uniform':
           r = sum([self.y[i[0]] for i in n_list]) / n #FIXME
           return r
           
        elif self.r_method == 'distance':
            total = [[(1/distance) * self.y[i], 1/distance] 
                                        for i, distance in n_list]
            total_rating = 0
            total_weight = 0
            for rating, weight in total:
                total_rating += rating
                total_weight += weight
            try:
                res = total_rating / (total_weight * n)
            except RuntimeWarning:
                print total_weight, n
            return res

        else:
            stderr.write("Unrecognized method used to calculate rating\n")
            exit(1)
    
    def __str__(self):
        s_m = self.sim_metric.func_name
        r_m = self.r_method
        return 'KNeighborRegressors\nk: %s\nsimilarity metric: %s\nrating evaluation:%s' % (self.k, s_m, r_m)




class KNeighborClassifier(BaseEstimator):
     
    #TODO : use *args & **kwds
    def __init__(self, X, y, k=3, sim_metric=sim_pearson, r_method='uniform'):
        super(KNeighborClassifier, self).__init__(X, y, k, sim_metric, r_method)
        print self

    def calculate_rating(self, n_list):

        #n = len(n_list)
        #cnt = Counter()
        class_labels = dict()

        if self.r_method == 'uniform':
            for i, distance in n_list:
                label = self.y[i]
                if label in class_labels:
                    class_labels[label] += 1
                else:
                    class_labels[label] = 1

        if self.r_method == 'distance':
            for i, distance in n_list:
                label = self.y[i]
                if label in class_labels:
                    try:
                        class_labels[label] += 1/distance 
                    except ZeroDivisionError:
                        class_labels[label] += 1/(distance + TOL)
                else:
                    class_labels[label] = 1

        #print class_labels
        label, occur = nlargest(1,class_labels.iteritems(),key=itemgetter(1))[0]
        #print label, occur
        return label

    def __str__(self):
        s_m = self.sim_metric.func_name
        r_m = self.r_method
        return 'KNeighborClassifier\nk: %s\nsimilarity metric: %s\nrating evaluation:%s' % (self.k, s_m, r_m)

