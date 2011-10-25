from __future__ import division
from utility import mae



class Evaluater(object):


    def __init__(self, rec, test_percentage=30):
        
        self.rec = rec
        self.n_instances = len(self.rec.X)
        self.n_test_item = int(self.n_instances * (test_percentage / 100))
        self.rec.X, self.testX = self.rec.X[:-self.n_test_item,:], self.rec.X[-self.n_test_item:,:]
        self.testy = self.rec.y[-self.n_test_item:] 
    
    def evaluate(self):

        #shuffle(self.rec.X) # First, dataset should be shuffled.
        result = []
        n = len(self.testX)
        for i, item in enumerate(self.testX):
            prediction = self.rec.predict(item)
            result.append(prediction)
            if (i+1) % 32 == 0:
                pass
                #print "%s/%s completed..." % (i, n)
        return mae(result, self.testy)




