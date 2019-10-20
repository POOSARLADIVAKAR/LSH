import time
import pandas as pd
import shingle
import preprocess
import signature
import minhashing

def main(): 
    # shingle_length = 4
    # preprocess.preprocess()

    time_start=time.time()
    # shingleDf = shingle.get_shingles(shingle_length)
    time_end=time.time()
    print(time_end-time_start)
    # shingleDf.to_pickle("./shingle_pickle4.py")
    # shingleDf.to_pickle("./shingle_pickle.py")
    # un_pickle_df=pd.read_pickle("./shingle_pickle.py")
    
    
    time_start=time.time()
    # signatureDf= minhashing.generate_signature_matrix(shingleDf,100)
    time_end=time.time()
    print(time_end-time_start)

    # signatureDf.to_pickle("./signature_pickle4shingles.py")
    # un_pickle_df=pd.read_pickle("./signature_pickle.py")

if (__name__=="__main__"):
    main()