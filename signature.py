import os
import pandas as pd
import random
from math import floor 
import numpy as np
import shingle

def get_hash_functions(num):
    hash_tup=[]
    for i in range(num):
        tup=(floor(random.uniform(1,num)),floor(random.uniform(1,num)))
        hash_tup.append(tup)
    return hash_tup

def get_hash_matrix(shingleDf,hash_list):
    new_df = shingleDf.copy()
    row = len(new_df.index)
    for i in range(len(hash_list)):
        new_col=[]
        for j in range(row):
            new_col.append((hash_list[i][0]*j+hash_list[i][1])%row)
        new_df["HASH"+str(i)]=new_col
    return new_df

def get_signature_matrix(shingleDf):

    # new_df = shingleDf.copy()
    
    signature_cols=["HASH_INDEX"]
    for i in shingleDf.columns:
        signature_cols.append(i)    
    signatureDf = pd.DataFrame(columns = signature_cols )
    signatureDf.set_index("HASH_INDEX",inplace=True)
    # print(signatureDf)

    hash_list = get_hash_functions(40)

    for i in range(len(hash_list)):
        signatureDf.loc["HASH"+str(i)]=[np.inf for j in range(len(shingleDf.columns))]

    # print(signatureDf) #signature matrix with rows as hash0 and cols as 
    # print(shingleDf.head(5))

    # return

    hash_matrix = get_hash_matrix( shingleDf , hash_list)
    # print(shingleDf.head(5))
    # print(hash_matrix.head(5))

    
    hash_matrix=hash_matrix.drop(shingleDf.columns,axis=1)
    # print(hash_matrix.head(5))

    # return
    # print(hash_matrix.head(5))
    # print(shingleDf.head(5))
    # print(signatureDf.head(5))
    # return

    row=len(shingleDf.index)
    hashes=len(hash_list)
    files=len(shingleDf.columns)

    for i in range(hashes): #hash_list[i]
        for j in range(row):
            for k in range(files):
                if(shingleDf.iloc[j][k]==1):
                    signatureDf.iloc[i][k]=min(signatureDf.iloc[i][k],hash_matrix.iloc[j][i])
    # print(signatureDf.head(5))
    return signatureDf


if __name__=='__main__':
    new_df=shingle.get_shingles(6)
    print(get_signature_matrix(new_df))