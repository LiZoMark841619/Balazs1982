import pydoc
import os
import sys
import pathlib
import datetime
from my_python.runtime import timer

def content(parent='current working directory'):
    '''
    This method does not require a parent directory as argumentum,
    because its default directory is the current working directory.
    The default value is a method which returns to the current WindowsPath
    directly, and the result of the content method is a return value of 
    one dictionary with directories as keys and every subfolder and file as values.
    '''
    
def read_files(dirs='directories'):
    '''
    This method requires the content() object's result and generate the open()
    objects by using the yield statement and the read() method.
    So the returned values are the data from every file in every folder
    under the parent directory.
    '''
    
class Jarmu:
    '''
    This is a parent/superclass of auto and bicikli subclasses. It is instantiated by
    type (auto or bicikli) and the counter increases everytime an object is being created.
    '''
    company_vehicles = 0
    def __init__(self, type: str) -> None:
        self.type = type
        Jarmu.company_vehicles += 1
        
    @staticmethod
    def day_of_registration():
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        D = dict(list(zip(range(1,8), days)))
        return D[datetime.datetime.now().isoweekday()]
    
class auto(Jarmu):
    '''
    This is a subclass of Jarmu superclass. It is instantiated by marka and ajtok_szama.
    The counter of auto and Jarmu increases everytime the object is created.
    '''
    count = 0
    
    def __init__(self, marka: str, ajtok_szama: int) -> None:
        Jarmu.__init__(self, 'auto')
        self.marka = marka
        self.ajtok_szama = ajtok_szama
        auto.count += 1
        
        
class bicikli(Jarmu):
    '''
    This is a subclass of Jarmu parent class. It is instantiated by marka and terhelhetoseg.
    The counter of bicikli and Jarmu increases everytime the object is created.
    '''
    count = 0 
    
    def __init__(self, marka: str, terhelhetoseg: int) -> None:
        Jarmu.__init__(self, 'bicikli')
        self.marka = marka
        self.terhelhetoseg = terhelhetoseg
        bicikli.count +=1

pydoc.writedoc('test')












