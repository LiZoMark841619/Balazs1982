import pydoc
import os
from pathlib import Path 
import pickle 
import random 

def content(parent=Path.cwd()):
    
    '''This method does not require a parent directory as attribute, because its default directory is the current working directory.
    The default value is a method which returns to the current WindowsPath directly, and the result of the content method is a return value of
    one dictionary with directories as keys and every subfolder and file as values'''
    
    return {root:(dir, file) for root, dir, file in os.walk(top=parent, topdown=False)}
s = '''
This is a folder-file searching code in which you can load in every data from every file. Moreover you can
make auto and bicikli objects by increasing the members of some fleet or picking new instances randomly. 
Then it will be saved in pickle file for later use. 
'''
pydoc.writedoc('docstring')




















