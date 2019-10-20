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
    files = pp.get_file_list('./temp')
   
    column_list=["SHINGLE"]
    for i in range(len(files)):
        column_list.append(files[i])
    shingle_df=pd.DataFrame(columns=column_list)
    shingle_df.set_index("SHINGLE",inplace=True)

    for i in tqdm(range(len(files))):
        file = open('./temp/'+files[i],"r")
        file_data = file.read()

        for j in tqdm(range( len(file_data) - (shingle_length-1) )):

            temp_str=file_data[j:j+shingle_length]
            if((temp_str in shingle_df.index)==False):
                shingle_df.loc[temp_str]=[ 0 for i in range(len(files)) ]
            shingle_df.at[temp_str,files[i]]= 1
    # print(shingle_df.head(5))
        file.close()
    return shingle_df

if __name__=='__main__':
    get_shingles(6)