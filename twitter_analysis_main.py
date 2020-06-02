import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np
import re
from glob import glob
import os
import earnings_scraper
import senti_ploter as myPloter
import top_words
import senti_process
import twitter_stats
import my_dictionary

os.chdir(os.getcwd()+"\\Twitter-Analysis-With-Earning-Event")
################################## parameters
key_word ="ZM" #"SBUX" #TTWO, "TGT","WMT",
ticker = 'ZM'
# 
save_senti_flag = 1 # if 1, it saves the sentiment text files by date and positivity 
is_show_top_words = 1 ; topn = 50 # show the top words for key words
influencer_threshold = 20 # define influencer with follower
# plot flags
is_plot = 1 # plot the graph
log_scale_flag= 0 # log-scale or not
is_earning_release = 0
is_show_stock_price = 1 # no stock processing would be much faster
#################################


if __name__ == "__main__":
    ####set path
    keyword_path = f"twitters\\{key_word}\\" # where the raw twitters are stored
    result_path = f"results\\{key_word}\\" # where the analysis results are stored

    # read all files
    files=glob(f'{keyword_path}*{key_word}*')
    # see all files'dates
    dates = [i[-14:-4] for i in files]

    print(f'We are observing data from {dates[0]} to {dates[-1]} for {key_word}')

    # read the sentiment dictionary, predownloaded
    pos_dic,neg_dic = my_dictionary.my_dict()
    # get all sentiment from all files, each file represent a day
    all_sentiments  = senti_process.get_all_senti(key_word,files,pos_dic,neg_dic,influencer_threshold,log_scale_flag,save_senti_flag)
    ###########################################################
    top_words.show_top(result_path,key_word,topn,is_show_top_words)
    #plot #####################################################
    if is_plot:myPloter.plotit(key_word,ticker,all_sentiments,is_show_stock_price,is_earning_release)
    # statits
    twi_daily = twitter_stats.daily_tweets(files)
    print(twi_daily)
    #plt.plot(twi_daily.date,twi_daily.twi_num);plt.show()
