#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd


# In[2]:


url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/electrification_by_province.csv'
ebp = pd.read_csv(url)

for col, row in ebp.iloc[:,1:].iteritems():
    ebp[col] = ebp[col].str.replace(',','').astype(int)

limpopo = ebp['Limpopo'].to_list()
limpopo = [float(x) for x in limpopo]

mpumalanga = ebp['Mpumalanga'].to_list()
mpumalanga = [float(x) for x in mpumalanga]

north_west = ebp['North west'].to_list()
north_west = [float(x) for x in north_west]

free_state = ebp['Free State'].to_list()
free_state = [float(x) for x in free_state]

kwazulu_natal = ebp['Kwazulu Natal'].to_list()
kwazulu_natal = [float(x) for x in kwazulu_natal]

eastern_cape = ebp['Eastern Cape'].to_list()
eastern_cape = [float(x) for x in eastern_cape]

western_cape = ebp['Western Cape'].to_list()
western_cape = [float(x) for x in western_cape]

northern_cape = ebp['Northern Cape'].to_list()
northern_cape = [float(x) for x in northern_cape]

gauteng = ebp['Gauteng'].to_list()
gauteng = [float(x) for x in gauteng]

url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/twitter_nov_2019.csv'
twitter_df = pd.read_csv(url)

dates = twitter_df['Date'].to_list()

def dictionary_of_metrics(data):

    mean = lambda data : sum(data)/len(data)
        
    maximum = lambda data : max(data)
    
    minimum = lambda data : min(data)
    
    def mid(data):
        data2 = sorted(data, reverse=False) 
        n = len(data)
        if n % 2 == 0: 
            m1 = data2[n//2] 
            m2 = data2[n//2 - 1] 
            median = (m1 + m2)/2
        else: 
            median = data2[n//2]
        return median
    
    def stdv(data):
        mean = sum(data)/len(data)
        t = 0.0
        for x in data:
            t = t + (x - mean)**2
        return (t/(len(data)-1))**0.5
    
    def var(data):
        mean = sum(data)/len(data)
        t = 0.0
        for x in data:
            t = t + (x - mean)**2
        v = t/(len(data)-1)
        return v
    
    met_dic = {'mean':mean(data), 'median':mid(data), 'variance':var(data),
               'standard deviation':stdv(data), 'min':minimum(data), 'max':maximum(data)}
    
    return met_dic

def five_num_summ(items):
    ### Code Here
    pass

def date_parser(list_dates):

  ### Code Here

  pass

def extract_municipality_hashtags(df):

  ### Code Here

  pass


def number_of_tweets_per_day(df):

  ### Code Here

  pass

def word_spliter(df):

  ### Code Here

  pass


def stop_words_http_remover(df):

  # Code Here

  pass

