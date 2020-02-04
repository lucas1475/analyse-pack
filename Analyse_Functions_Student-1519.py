#!/usr/bin/env python
# coding: utf-8
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

