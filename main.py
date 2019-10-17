import time
import pandas as pd
import shingle
import preprocess
import signature

def main(): 
    shingle_length = 6

    # preprocess.preprocess()

    time_start=time.time()
    shingleDf = shingle.get_shingles(shingle_length)
    time_end=time.time()
    print(time_end-time_start)

    shingleDf.to_pickle("./shingle_pickle.py")
    un_pickle_df=pd.read_pickle("./shingle_pickle.py")
    print(un_pickle_df)
    
    
    time_start=time.time()
    signatureDf= signature.get_signature_matrix(shingleDf)
    time_end=time.time()
    print(time_end-time_start)

    signatureDf.to_pickle("./signature_pickle.py")
    un_pickle_df=pd.read_pickle("./signature_pickle.py")
    print(un_pickle_df)

if (__name__=="__main__"):
    main()