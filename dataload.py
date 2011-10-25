#! /usr/bin/python
# -*- coding: utf-8 -*-

from numpy.random import shuffle
import numpy as np

DATA_FOLDER = 'data/'


def readdata2array(filename='dataspam', delimiter=None, missing_values=None):
    """
        Read data file and return the whole array.
    """
    return np.genfromtxt(DATA_FOLDER + filename, delimiter = delimiter, \
                         missing_values=missing_values)


def getXy(filename='dataspam', y_index=-1, delimiter=None):
    
    """
        output:
            -> X: array (design matrix)
            -> y: 1d-array (class labels of each instance)
    """
    data = readdata2array(filename, delimiter=delimiter)
    shuffle(data)
    X = data[:,0:y_index]
    y = data[:,y_index]
    #X = data[:,1:]
    #y = data[:,0]
    return X, y
