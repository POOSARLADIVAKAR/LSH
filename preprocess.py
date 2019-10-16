import pandas as pd
import os
import re

def get_file_list(dir):
    files = os.listdir(dir)
    files.reverse()
    return files

def preprocess():
    file_list = get_file_list('./temp')
    for i in range(len(file_list)):
        file_path='./temp/'+file_list[i]
        file=open(file_path,"r+")
        file_data=file.read()

        file_data=file_data.lower()
        file_data=re.sub(r'[,.\n\s ]',"",file_data)

        file.seek(0)
        file.write(file_data)
        file.truncate()
        file.close()
        
if __name__=='__main__':
    preprocess()