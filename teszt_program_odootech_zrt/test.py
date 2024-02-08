import pydoc
import os
import random
import pickle
from pathlib import Path 


def content(parent='current working directory'):
    
    '''
    This method does not require a parent directory as argumentum, because its default directory is the current working directory.
    The default value is a method which returns to the current WindowsPath directly, and the result of the content method is 
    a return value of one dictionary with directories as keys and every subfolder and file as values.
    '''
    
def read_files(dirs='directories'):
    
    '''
    This method requires the content() object's result and generate the open() objects by using the yield statement and the read() method.
    So the returned values are the data from every file in every folder under the parent directory.
    '''
    
class Jarmu:
    '''
    This is a parent class of auto and
    bicikli subclasses. It is instantiated by
    type (auto or bicikli) and the counter
    increases everytime an object is being created.
    '''
    registered_vehicle = 0
    
    def __init__(self, type: str) -> None:
        self.type = type
        
class auto(Jarmu):
    '''
    This is a subclass of Jarmu parent class.
    It is instantiated by ajtok_szama and marka.
    The counter of auto and Jarmu increases everytime
    the object is created.
    '''
    count = 0
    
    def __init__(self, ajtok_szama: int, marka: str) -> None:
        super().__init__(type)
        self.ajtok_szama = ajtok_szama
        self.marka = marka
        auto.count += 1
        Jarmu.registered_vehicle += 1
            
    def vehicle_data(self) -> dict:
        return {'type':'auto', 'ajtok_szama':self.ajtok_szama, 'marka':self.marka}
    
class bicikli(Jarmu):
    '''
    This is a subclass of Jarmu parent class.
    It is instantiated by terhelhetoseg and marka.
    The counter of bicikli and Jarmu increases everytime
    the object is created.
    '''
    count = 0 
    
    def __init__(self, terhelhetoseg: int, marka: str) -> None:
        super().__init__(type)
        self.terhelhetoseg = terhelhetoseg
        self.marka = marka
        bicikli.count +=1
        Jarmu.registered_vehicle +=1
    
    def vehicle_data(self) -> dict:
        return {'type':'bicikli', 'terhelhetoseg':self.terhelhetoseg, 'marka':self.marka}

pydoc.writedoc('test')





