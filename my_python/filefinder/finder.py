import pathlib
import os
import pandas as pd

while True:
    file_options = ['.csv', '.excel', '.sql']
    file_suffix = input(f'Enter a valid suffix from {file_options} options to search for those files! ')
    target = []
    
    for roots, dirs, files in os.walk(top=pathlib.Path.cwd(), topdown=True):
        target = [file for file in files if file_suffix in file]
    if file_suffix in file_options and target: break
    else: print(f'Sorry, there is no such file with {file_suffix} suffix, try another one! ')
    continue

while True:
    answer = input(f'Please enter a valid filename from {target} files to load in and make a pandas dataframe! ')
    
    if answer in target: 
        if '.csv' in answer: df = pd.read_csv(answer, encoding='utf-8'); break
        elif '.excel' in answer: df = pd.read_excel(answer); break
        elif '.sql' in answer: df = pd.read_sql(answer); break
            
print(f'GOOD JOB! You have just transformed {answer} into a pandas DataFrame.\n')