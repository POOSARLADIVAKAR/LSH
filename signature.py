import os
import pandas as pd
import random
from math import floor 
import numpy as np
import shingle
from tqdm import tqdm

def get_hash_functions(num):
    hash_tup=[]
    print("This is get_hash_functions")
    for i in tqdm(range(num)):
        tup=(floor(random.uniform(1,num)),floor(random.uniform(1,num)))
        hash_tup.append(tup)
    return hash_tup

def get_hash_matrix(shingleDf,hash_list):
    print("this is get_hash_matrix function")
    new_df = shingleDf.copy()
    row = len(new_df.index)
    for i in tqdm(range(len(hash_list))):
        new_col=[]
        for j in tqdm(range(row)):
            new_col.append((hash_list[i][0]*j+hash_list[i][1])%row)
        new_df["HASH"+str(i)]=new_col
    return new_df

def get_signature_matrix(shingleDf):
    
    # hash_list = get_hash_functions(100)
    # hash_functions_df = pd.DataFrame(hash_list)
    # hash_functions_df.to_pickle("./hash_functions.py")
    hash_functions_df=pd.read_pickle("./hash_functions.py")
    hash_list = []
    for i in hash_functions_df.index:
        hash_list.append((hash_functions_df.iloc[i][0],hash_functions_df.iloc[i][1]))
    # print(hash_list)

    signature_cols=["HASH_INDEX"]
    for i in shingleDf.columns:
        signature_cols.append(i)    
    signatureDf = pd.DataFrame(columns = signature_cols )
    signatureDf.set_index("HASH_INDEX",inplace=True)

    for i in range(len(hash_list)):
        signatureDf.loc["HASH"+str(i)]=[np.inf for j in range(len(shingleDf.columns))]

    # hash_matrix = get_hash_matrix( shingleDf , hash_list)
    # hash_matrix.to_pickle("./hash_matrix.pkl")
    hash_matrix = pd.read_pickle("./hash_matrix.pkl")
    hash_matrix=hash_matrix.drop(shingleDf.columns,axis=1)
    # print(hash_matrix.head(5))

    row=len(shingleDf.index)
    hashes=len(hash_list)
    files=len(shingleDf.columns)

    for i in tqdm(range(hashes)): #hash_list[i]
        for j in tqdm(range(row)):
            for k in tqdm(range(files)):
                if(shingleDf.iloc[j][k]==1):
                    signatureDf.iloc[i][k]=min(signatureDf.iloc[i][k],hash_matrix.iloc[j][i])
    # print(signatureDf.head(5))
    return signatureDf


if __name__=='__main__':
    # new_df=shingle.get_shingles(6)
    # print(get_signature_matrix(new_df))
    signature_mat = pd.read_pickle("./sig_mat.pickle")
    print(signature_mat.shape)
    print(signature_mat[1:10])