import numpy as np
import math

class Stats:
    
    def __init__(self, list):
        self.list = list
        
    def min(self):
        return np.min(self.list)
        
    def median(self):
        a = self.list
        if len(a) % 2 == 0:
            return (a[len(a)//2] + a[len(a)//2 -1])/2
        else:
            return a[len(a)//2]
         
    def mean(self):
        return np.mean(self.list)
    

list_1 = Stats([10, 20, 30, 40, 40, 40, 50])
list_2 = Stats([100, 90, 150, 250, 200])
print(list_1.median())
print(list_2.median())
print(list_1.min())
print(list_1.mean())
            
    