import time
import pandas as pd
import shingle
import preprocess
import signature
import minhashing
import lsh
import os

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

    shingle_length = 4  #set shingle length 
    if os.path.exists("./shingle_pickle4.py") == False :

        time_start=time.time()
        preprocess.preprocess('./temp')  #Time calculation for pre processing files
        time_end=time.time()
        print(time_end-time_start)   # 0.01327657699584961

    if os.path.exists("./shingle_pickle4.py") == False :
            
        time_start=time.time()
        shingleDf = shingle.get_shingles(shingle_length) #Time calculation fro shingling
        time_end=time.time()
        print(time_end-time_start)  # 207.01369958496123463
        # shingleDf.to_pickle("./shingle_pickle4.py")
        # shingleDf.to_pickle("./shingle_pickle.py")
        # un_pickle_df=pd.read_pickle("./shingle_pickle.py")
    
    if os.path.exists("./shingle_pickle4.py") == False :

        time_start=time.time()
        signatureDf= minhashing.generate_signature_matrix(shingleDf,100) # Time calculation for min hashing
        time_end=time.time()
        print(time_end-time_start) # 2041.65769958496173297

        # signatureDf.to_pickle("./signature_pickle4shingles.py")
        # un_pickle_df=pd.read_pickle("./signature_pickle.py")

    output0 = "Please Enter document number : " # taking user input query and threshold jaccard score
    print(output0)
    query = (int)(input()) 
    output1 = "Please Enter threshold jscore: "
    print(output1)
    sig_matrix=pd.read_pickle("./sig_matc_4shigles.pickle")
    jscore = (float)(input()) 
    for i in range(query,query+1):
        similar_documents = lsh.lsh(sig_matrix,sig_matrix.columns[i],100) # applying Lsh on signature matrix
        print(similar_documents)
        if(len(similar_documents)==0):
            print("No similar Documents found")
        else:    
            p_count = lsh.precision(similar_documents,sig_matrix.columns[i],jscore = 0.1) #calculating precision for retreivs documents
            print("precision is = "+ (str)(p_count/len(similar_documents)))
            r_count = lsh.recall(sig_matrix.columns,sig_matrix.columns[i],jscore = 0.1 ) #calculating recall for retreived documents
            print("recall is = "+ (str)(p_count/r_count))



if (__name__=="__main__"):
    main()