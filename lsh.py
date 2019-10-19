import math
import numpy as np
import pandas as pd

# def bands_rows(jscore,n_doc):
#     # blog b = -n*log jscore
#     err=np.inf
#     b_actual=1
#     print(err,b_actual,jscore,n_doc)
#     print(n_doc*math.log(jscore,10))
#     for i in range(1,n_doc+1):
#         if (i*(math.log(i,10))+n_doc*(math.log(jscore,10)))<err :
#             err=i*(math.log(i,10))+n_doc*(math.log(jscore,10))
#             b_actual=i
#     return (b_actual,n_doc//b_actual)

def bands_rows(n_doc):
    factors=[]
    for i in range(1,(int)(math.sqrt(n_doc)+1)):
        if n_doc%i==0:
            factors.append((i,n_doc//i))
    return factors

def lsh(signatureDf, query, jscore,n_doc):
    factors_ndoc = bands_rows(n_doc)
    # print(factors_ndoc)
    # print("----------")
    # print("----------")
    for i in range(len(factors_ndoc)):
        bands = factors_ndoc[i][0]
        rows = factors_ndoc[i][1]
        similar_docs= dict()
        # bands=5
        # rows=8
        print(bands,rows)
        for j in range(bands):
            bucket_dictonary= dict()
            count = j * rows
            print(count)
            for k in range(len(signatureDf.columns)): #push doc id's so doc name found by signatureDf.columns[k]
                
                signature_tup = (tuple)(signatureDf.iloc[count : count+rows][signatureDf.columns[k]])
                print(signature_tup)
                hash_val = hash(signature_tup)
                hash_val = 1896222623651181975

                if hash_val in bucket_dictonary:
                   bucket_dictonary[hash_val].append(k)
                else:
                   bucket_dictonary[hash_val]= [k]
                print(bucket_dictonary)
            # return
            query_tup = tuple(signatureDf.iloc[count:count+rows][query])
            query_hash_val = hash(query_tup)
            print(query_hash_val)
            query_hash_val = 1896222623651181975
            
            for k in range(len(bucket_dictonary[query_hash_val])):  #here k is elements in bucket so document accessed by sigDf[ bucket_dic[query_hash_val][k] ]
                file = signatureDf.columns[bucket_dictonary[query_hash_val][k]]
                if (file!= query):
                    if file not in similar_docs:
                        similar_docs[file]=1
                    else:
                        similar_docs[file]+=1
                    # print()
        print("----------")
        print("----------")
        # return
        # similar_docs = (set)(similar_docs)
        print(similar_docs)
        # evaluation(similar_docs)
    # return evaluated_similar_docs


if __name__=='__main__':
    un_pickle_df=pd.read_pickle("./signature_pickle.py")
    # print(un_pickle_df)
    similar_documents = lsh(un_pickle_df, "file2", 1,40)
    # evaluation


