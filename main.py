import time
import pandas as pd
import shingle
import preprocess
import signature

def main(): 
    shingle_length = 6

    # preprocess.preprocess()

    # time_start=time.time()
    # shingleDf = shingle.get_shingles(shingle_length)
    # time_end=time.time()
    # print(time_end-time_start)
    # print(shingleDf.head(5))
    # shingleDf.to_pickle("./shingle_pickle.py")
    un_pickle_df=pd.read_pickle("./shingle_pickle.py")
    # print(un_pickle_df.head(10))
    
    
    time_start=time.time()
    signatureDf= signature.get_signature_matrix(un_pickle_df)
    time_end=time.time()
    print(time_end-time_start)
    print(signatureDf.head(5))
    print(len(signatureDf.index))

    signatureDf.to_pickle("./signature_pickle.py")
    # un_pickle_df=pd.read_pickle("./signature_pickle.py")
    # print(un_pickle_df.head(5))

if (__name__=="__main__"):
    main()