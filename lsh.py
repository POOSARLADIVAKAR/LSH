import math
import numpy as np
import pandas as pd
from tqdm import tqdm

def bands_rows(jscore,n_doc):
    """
        This function finds best Bands and Rows value for My S shaped Prbabilty function  (1- (1-s^r)^b)\n
        This is found by finding B and R that are integers and satisying (1/b)^(1/r)

        Parametrs
        ---------
        jscore : float
            User threshold for jaccard similarity score between two documents 

        n_doc : int
            Number of documents in the Corpus and (n_doc = b*r)
        
        Returns
        -------
        (b,r) : tuple
        Returns Best tuple of (bands,rows) that is closest to (1/b)^1/r
    """
    # blog b = -n*log jscore
    err=np.inf
    b_actual=1
    print(err,b_actual,jscore,n_doc)
    print(n_doc*math.log(jscore,10))
    for i in range(1,n_doc+1):
        if (i*(math.log(i,10))+n_doc*(math.log(jscore,10)))<err :
            err=i*(math.log(i,10))+n_doc*(math.log(jscore,10))
            b_actual=i
    return (b_actual,n_doc//b_actual)  # givin output always 1

def bands_rows(n_doc):
    """
        This fuuctio finds all factors of _doc

        Parametrs
        ---------

        n_doc : int
            Number of documents in the Corpus and (n_doc = b*r)
        
        Returns
        -------
        factors : List[] 
        List of tuples of all the factors of n_doc input representing (bands,rows) tuple
    """
    factors=[]
    for i in range(1,(int)((n_doc)+1)):
        if n_doc%i==0:
            factors.append((i,n_doc//i))
    return factors

def lsh(signatureDf, query,n_doc):
    """
        This function finds all the similar documents for your query document for all the values combinations of  Bands and Rows 

        Parametrs
        ---------
        signatureDf: pandas. Dataframe
            DataFrame of Signatures Obtained after applying minhashing on Shingle Matrix
        Query : string
            String Representing fileame to which User is trying to find similar Documents

        n_doc : int
            Number of documents in the Corpus and (n_doc = b*r)
        
        Returns
        -------
        similar_docs : Dictionary
        Returns Dictionary of documets that are similar to Query document
        Key = filename 
        value = number of bands in which both query and file got hashed to same bucket
    """

    factors_ndoc = bands_rows(n_doc)
    evaluated_similar_docs = dict()
    
    # for i in range(len(factors_ndoc)):
    for i in range(7,8):
        bands = factors_ndoc[i][0]
        rows = factors_ndoc[i][1]
        similar_docs= dict()
        
        for j in range(bands):
            bucket_dictonary= dict()
            count = j * rows
        
            for k in range(len(signatureDf.columns)): #push doc id's so doc name found by signatureDf.columns[k]
                
                signature_tup = (tuple)(signatureDf.iloc[count : count+rows][signatureDf.columns[k]])
                hash_val = hash(signature_tup)
                if hash_val in bucket_dictonary:
                   bucket_dictonary[hash_val].append(k)
                else:
                   bucket_dictonary[hash_val]= [k]
                
            query_tup = tuple(signatureDf.iloc[count:count+rows][query])
            query_hash_val = hash(query_tup)
            
            for k in range(len(bucket_dictonary[query_hash_val])):  #here k is elements in bucket so document accessed by sigDf[ bucket_dic[query_hash_val][k] ]
                file = signatureDf.columns[bucket_dictonary[query_hash_val][k]]
                if (file!= query):
                    if file not in similar_docs:
                        similar_docs[file]=1
                    else:
                        similar_docs[file]+=1
        # print("----------")
        # print("----------")
        print(similar_docs)
        # evaluated_similar_docs = similar_docs
        print(len(similar_docs))
    #     if (len(similar_docs)>=1) & (rows!=1) :
    #         precision(similar_docs,query,0.5)
    #         evaluated_similar_docs = similar_docs
    # return evaluated_similar_docs
    return similar_docs

def find_score(doc1,doc2):
    """
        This function finds the jaccard similarity score between two documents

        Parametrs
        ---------
        Doc1,Doc2: string
            strings represeting documents names
        
        Returns
        -------
        jaccard_score : float
        Returns jaccard score by finding union and intersection of all the shingles between two documents
    """
    intersection = 0
    union = 0
    rows_df,columns_df = shingleDF.shape 
    for i in tqdm(range(rows_df)):
        if shingleDF.iloc[i][doc1] ==1 |  shingleDF.iloc[i][doc2] ==1 :
            union+=1
        if shingleDF.iloc[i][doc1] ==1 &  shingleDF.iloc[i][doc2] ==1 :
            intersection+=1
    return intersection/union

def precision(similar_docs,query,jscore):
    """
        This functions finds number of relevant documents in all the returned documents from lsh function

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
    # shingleDF = pd.read_pickle("./shingle_pickle.py")
    jscore_dict = dict()
    keys_list = similar_docs.keys()
    count = 0
    for i in keys_list:
        sim_score = find_score(query , i)
        if sim_score>= jscore:
            count+=1    
    return count
        
def recall(columns,query,jscore):
    """
        This functions finds number of relevant documents to query document in whole corpus
        
        Parametrs
        ---------
        columns: List[]
            List of all the file names in corpus
        query: string
            string representig query document's file name
        jscore : float
            User threshold for jaccard similarity score between two documents 

        Returns
        -------
        recall_count : int
        Returns number of documents from whole corpus whose jaccard score is greater than user jscore input
    """
    recall_count=0
    for i in columns:
        if i!=query:
            sim_score = find_score(i,query)
            if sim_score > jscore:
                recall_count+=1
    return recall_count




if __name__=='__main__':
    sig_matrix=pd.read_pickle("./sig_matc_4shigles.pickle")
    # print(sig_matrix.head(5))
    shingleDF = pd.read_pickle("./shingle_pickle4.py")
    # print(shingleDF.head(5))
    # print(find_score("g4pD_taskd.txt", "g3pB_taska.txt" ))
    # for i in sig_matrix.columns:
    output0 = "Please Enter document number : "
    print(output0)
    query = (int)(input()) 
    output1 = "Please Enter threshold jscore: "
    print(output1)
    jscore = (float)(input()) 
    for i in range(query,query+1):
        similar_documents = lsh(sig_matrix,sig_matrix.columns[i],100)
        print(similar_documents)
        p_count = precision(similar_documents,sig_matrix.columns[i],jscore = 0.1)
        print("precision is = "+ (str)(p_count/len(similar_documents)))
        r_count = recall(shingleDF.columns ,sig_matrix.columns[i],jscore = 0.1 )
        print("recall is = "+ (str)(p_count/r_count))
    # evaluation
    # print(bands_rows(100))