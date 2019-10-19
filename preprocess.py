import pandas as pd
import os
import re
import time
from os import walk

def get_file_list(dir):
    files = os.listdir(dir)
    # files.reverse()
    print(files)
    return files

    

def preprocess():
    file_list = get_file_list('./temp')
    print(file_list)
    for i in range(len(file_list)):
        file_path='./temp/'+file_list[i]
        with open(file_path, encoding="utf8", mode="r+" ,errors='ignore') as file:
            print(file)
            file_data = file.read()
            file_data=file_data.lower()
            print(file_data[0])
            file_data = re.sub(r'[,.\'"()\n\s \r\t?;:-`”‘’“-]',"",file_data)
            # print(file_data)
            file.seek(0)
            file.write(file_data)
            file.truncate()
        # return
        
if __name__=='__main__':
    time_start=time.time()
    # get_file_list("./temp")
    preprocess()
    time_end=time.time()
    print(time_end-time_start)
    