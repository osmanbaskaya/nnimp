#! /usr/bin/python
# -*- coding: utf-8 -*-

from utility import sim_pearson

class BaseEstimator(object):

    
    def __init__(self, X, y, k=3, sim_metric=sim_pearson, r_method='uniform'):

        self.X = X
        self.y = y
        self.k = k
        self.sim_metric = sim_metric
        self.r_method = r_method


    def find_neighbors(self, a):
        neighbors = []
        for i, candidate in enumerate(self.X):
            distance = self.sim_metric(a, candidate)
            neighbors.append((i, distance, ))
        
        # It should be compared whether sim_metric is correlation or
        # distance metric. If pearson`s correlation coeff. is picked
        # neighbors should be sorted by reverse order.
        rev_order = BaseEstimator.ret_neighbors(self.sim_metric)

        #sorting by the distances.
        neighbors.sort(key = lambda n: n[1], reverse=rev_order)
        return neighbors[1:self.k + 1] # 1 because first element
                                                      # is always a itself.
    @staticmethod
    def ret_neighbors(metrics):

        rev_order = False
        if metrics.func_name in ('sim_pearson',):
            rev_order = True
        return rev_order

    
    def predict(self, a):
        self.a = a
        neighbors = self.find_neighbors(a)
        return self.calculate_rating(neighbors)
    #def predict(self):
        #raise NotImplementedError("The %s method should be overriden" \
                                #% self.predict.func_name)


