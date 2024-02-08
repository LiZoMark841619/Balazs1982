import pydoc
import os
import random
import pickle
from pathlib import Path 


def content(parent='current working directory'):
    
    '''
    This method does not require a parent directory as attribute, because its default directory is the current working directory.
    The default value is a method which returns to the current WindowsPath directly, and the result of the content method is 
    a return value of one dictionary with directories as keys and every subfolder and file as values.
    '''
    
    return {root:(dir, file) for root, dir, file in os.walk(top=parent, topdown=False)}
pydoc.writedoc('test')


