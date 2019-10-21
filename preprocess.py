import pandas as pd
import os
import re
import time
from os import walk
from tqdm import tqdm

def get_file_list(dir):
    """
        This function gets List of all files in a directory

        Parametrs
        ---------
        Dir:
            Directory path  in workspace containing all Documents
        
        Returns
        -------
        files: List
        Returns List of all files in a directory
    """
    files = os.listdir(dir)  # lists all files in the directory
    # files.reverse()
    print(files)
    return files
    
def preprocess(temp):
    """
        This function preprocess all files and overwrites the original files\n
        This is done by using custom regular expression to elemenate useless charecters from file

        Parametrs
        ---------
        NULL

        Returns
        -------
        NULL
    """
    print(tqdm)
    file_list = get_file_list(temp)
    # print(file_list)
    for i in tqdm(range(len(file_list))):
        file_path='./temp/'+file_list[i]
        with open(file_path, encoding="utf8", mode="r+" ,errors='ignore') as file: #openining encoding files by ignoring errors
            print(file)
            file_data = file.read()
            file_data=file_data.lower()
            # print(file_data[0])
            file_data = re.sub(r'[\n\r\s ,.;"\'’”()|/]',"",file_data) #regex to remove unnecessary charecters in file

            # print(file_data)
            file.seek(0)  #sets file current positon to 0 so new data overwrites original data
            file.write(file_data) # writing data back to file
            file.truncate()  #truncate until current positon of file (input descriptor)
        # return
        
if __name__=='__main__':
    time_start=time.time()
    # get_file_list("./temp")
    preprocess()
    time_end=time.time()
    print(time_end-time_start)
    