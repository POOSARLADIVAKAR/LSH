import os
import pandas as pd
import preprocess as pp
from tqdm import tqdm

def get_shingles(shingle_length):
    """
        This funciton generates a shingle DataFrame by fiding all shingles in all the files and their incidences

        Parametrs
        ---------
        Shingle_length: int
            length of  shingle Etries in Dataframe (Indices of Data frame)
        
        Returns
        -------
        shingle_Df: Pandas.Dataframe
        Returns Shingle Dataframe by finding all shingle by traversing all files in directory tmep
    """
    files = pp.get_file_list('./temp') #preprocessing temp folder files
   
    column_list=["SHINGLE"]
    for i in range(len(files)):
        column_list.append(files[i])
    shingle_df=pd.DataFrame(columns=column_list) #create empty data frame with structure
    shingle_df.set_index("SHINGLE",inplace=True) # set index of data frame to shingle
 
    for i in tqdm(range(len(files))): #runnign through all files O(number of files*file_size)
        file = open('./temp/'+files[i],"r")
        file_data = file.read()

        for j in tqdm(range( len(file_data) - (shingle_length-1) )): #running through all shingles in a file O(shigle_len)

            temp_str=file_data[j:j+shingle_length]
            if((temp_str in shingle_df.index)==False):
                shingle_df.loc[temp_str]=[ 0 for i in range(len(files)) ]
            shingle_df.at[temp_str,files[i]]= 1 #faster than shingleDf.iloc[i][j]
    # print(shingle_df.head(5))
        file.close()
    return shingle_df

if __name__=='__main__':
    get_shingles(6)