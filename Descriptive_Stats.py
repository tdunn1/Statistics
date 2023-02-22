# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:11:13 2023

@author: Tim
"""
from math import sqrt

class Stat_Descrip(object):
    """Descriptive statistics for data.
    
       Parameters
       ----------
       is_sample : boolean 
           determines wheather data is a population(False) or 
           a sample(True)
          
       Attributes
       ----------
       average : float
           data average
       variance : float
           data variance
       std_dev : float
           data standard deviation
     """
    def __init__(self,is_sample:bool = False):
         self.is_sample = is_sample
         
    def Stats(self, data):
        """calculates descriptive statistics
        
        Parameters
        ----------
        data : list
            floats and integers to caclulate statistics
            
        Returns
        -------
        self : object
        """
        self.avg = self.Average(data)
        self.var = self.Variance(data)
        self.std_dev = self.Std_Dev(data)
        return self
    
    def Average(self, data):
        """returns average"""
        return sum(data)/len(data)
    
    def Variance(self,data):
         """returns data variance"""
         return sum((self.avg - x)**2 for x in data)/(len(data)
                                                 -(1 if self.is_sample else 0))
    
    def Std_Dev(self,data):
         """returns data standard deviation"""
         return sqrt(self.var)
    

if __name__ == '__main__':
    data = [0,1,2,3,4,5]
    X = Stat_Descrip()
    X = X.Stats(data)
    print(X.avg, X.var, X.std_dev)


    
    