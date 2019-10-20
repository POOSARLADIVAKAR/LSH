"""
Reduce the size of shingle incidence matrix by converting docs to signatures

This module calculates the signature of each document using minhashing 
technique by utilizing a number of hash functions

This module contatins following functions:
    * generate_signature_matrix - to generate signature matrix from incidence 
        matrix
"""
import pandas as pd
from random import randint
from pandas import DataFrame, read_pickle
import numpy as np
import os
from tqdm import tqdm
from math import floor
import random
import sys

def generate_hash_functions(rows, no_of_hash_functions):
    """This function generates parameters for given no of hash functions
    
    Parameters
    ----------
    rows: int
        no of shingles in corpus, a.k.a no of rows in shingle matrix
    no_of_hash_functions: int, optional
        no of hash functions to generate for minhashing
        Default: 100
    
    Returns
    -------
    list
        list of functions which can be used as hashes[i](x)
    """

    hashes = []
    c = rows
    
    # all functions are same here. check this
    for i in range(no_of_hash_functions):
        def hash(x):
            """
            This function calculates hash for given x

            hash function format: (a*x+b)%c where
                c: prime integer just greater than rows
                a,b: random integer less than c
            """
            # return ((floor(random.uniform(1,sys.maxsize)))*x+(floor(random.uniform(1,sys.maxsize))))%c
            return (randint(1,2*c)*x + randint(1,2*c))%c
        hashes.append(hash)

    return hashes


def generate_signature_matrix(incidence_matrix, no_of_hash_functions):
    """This function generates the signature matrix for whole corpus

    if a already generated pickle file named sig_mat.pickle exists,
    this function will load it instead

    Parameters
    ----------
    incidence_matrix: pandas.DataFrame
        incidence index generated after shingling of similar process
    no_of_hash_functions: int, optional
        no of hash functions to use to generate document signatures.
        Default: 100
    
    Returns
    -------
    pandas.DataFrame
        dataframe containing signatures of each document
    """

    # is pickle file exists, load and return it
    # if os.path.exists("sig_mat.pickle"):
    #     signature_matrix = read_pickle("sig_mat.pickle")
    #     print("Using already created sig_mat.pickle file")
    #     return signature_matrix

    rows, cols = incidence_matrix.shape
    hashes = generate_hash_functions(rows, no_of_hash_functions)
    signature_matrix = DataFrame(index=[i for i in range(no_of_hash_functions)], columns=incidence_matrix.columns)
    
    # core minhashing algorithm
    for i in tqdm(range(rows)):
        for j in incidence_matrix.columns:
            if incidence_matrix.iloc[i][j]==1:
                
                for k in range(no_of_hash_functions):
                    
                    if np.isnan(signature_matrix.iloc[k][j]):
                        signature_matrix.iloc[k][j] = hashes[k](i)
                        # print(hashes[k](i))
                    else:
                        signature_matrix.iloc[k][j] = min(signature_matrix.iloc[k][j], hashes[k](i))
                        # print(hashes[k](i))
    
    print("saving generated signature_matrix to pickle file...")
    signature_matrix.to_pickle("./sig_matc_4shigles.pickle")
    # print("saved to sig_mat.pickle")
    return signature_matrix

if __name__=="__main__":
    incidence_matrix=pd.read_pickle("./shingle_pickle.py")
    signature_mat = generate_signature_matrix(incidence_matrix,100)
    print(signature_mat.head(5))
