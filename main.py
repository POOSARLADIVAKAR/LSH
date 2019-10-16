import time
import pandas as pd
import shingle
import preprocess

def main(): 
    shingle_length = 6

    # preprocess.preprocess()
    
    time_start=time.time();
    shingleDf = shingle.get_shingles(shingle_length)
    time_end=time.time();
    print(time_end-time_start)

    # shingleDf.to_pickle("./temp_pickle.py")
    # un_pickle_df=pd.read_pickle("./temp_pickle.py")
    # print(un_pickle_df)

if (__name__=="__main__"):
    main()