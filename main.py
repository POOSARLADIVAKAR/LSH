import time
import pandas as pd
import shingle
import preprocess
import signature
import minhashing

def main(): 
    """
        This functions is main function in your folder which should run first
        calls other functions and calculate time taken to execute for evry function call and serializing all Dataframes obtained

        Parametrs
        ---------
        similar_docs: Python Dictionary()
            Dictionary of similar documents to Query Document
        query: string
            string representig query document's file name
        jscore : float
            User threshold for jaccard similarity score between two documents 

        
        Returns
        -------
        Precision_count : int
        Returns number of documents from input similar_docs dictionary that have higher jaccard score than User threshold
    """
    shingle_length = 4
    time_start=time.time()
    preprocess.preprocess()
    time_end=time.time()
    print(time_end-time_start)   # 0.01327657699584961
    return 
    time_start=time.time()
    shingleDf = shingle.get_shingles(shingle_length)
    time_end=time.time()
    print(time_end-time_start)  # 207.01369958496123463
    # shingleDf.to_pickle("./shingle_pickle4.py")
    # shingleDf.to_pickle("./shingle_pickle.py")
    # un_pickle_df=pd.read_pickle("./shingle_pickle.py")
    
    
    time_start=time.time()
    signatureDf= minhashing.generate_signature_matrix(shingleDf,100)
    time_end=time.time()
    print(time_end-time_start) # 2041.65769958496173297

    # signatureDf.to_pickle("./signature_pickle4shingles.py")
    # un_pickle_df=pd.read_pickle("./signature_pickle.py")

if (__name__=="__main__"):
    main()