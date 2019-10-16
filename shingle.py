import os
import pandas as pd
import preprocess as pp

def get_shingles(shingle_length):
    files=pp.get_file_list('./temp')
    column_list=["shingle"]
    for i in range(len(files)):
        column_list.append(files[i])
    shingle_df=pd.DataFrame(columns=column_list)
    shingle_df.set_index("shingle",inplace=True)
    for i in range(len(files)):
        file = open('./temp/'+files[i],"r")
        file_data = file.read()
        for j in range( len(file_data) - (shingle_length-1) ):
            temp_str=file_data[j:j+shingle_length]
            if((temp_str in shingle_df.index)==False):
                # print(temp_str)
                shingle_df.loc[temp_str]=[ 0 for i in range(len(files)) ]
            shingle_df.at[temp_str,files[i]]= 1
    # print(shingle_df)
    return shingle_df

if __name__=='__main__':
    get_shingles(6)