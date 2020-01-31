#!/usr/bin/env python
# coding: utf-8

# # Analyse : Predict
# 
# Functions are important in reducing the replication of code as well as giving the user the functionality of getting an ouput on varying inputs. The functions you will write all use Eskom data/variables.
# 
# For the predict, you will need to write 7 functions. These functions are:
# 
# 1. Metric Dictionary
# 2. Five Number Summary Dictionary
# 3. Date Parser
# 4. Hashtag & Municipality Remover
# 5. Number of Tweets per Day
# 6. Word Splitter
# 7. Stopwords & Link Remover
# 

# In[1]:


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


# In[3]:


url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/twitter_nov_2019.csv'
twitter_df = pd.read_csv(url)

dates = twitter_df['Date'].to_list()


# # Function 1: Metric Dictionary
# 
# Write a function which takes in a list of integers and returns a dictionary of the mean, median, variance, standard deviation, min and max. Answers should be rounded to the second decimal.
# 
# _**Expected Output**_:
# 
# ```python
# gauteng = [39660.0,
#             36024.0,
#             32127.0,
#             39488.0,
#             18422.0,
#             23532.0,
#             8842.0,
#             37416.0,
#             16156.0,
#             18730.0,
#             19261.0,
#             25275.0]
# 
# dictionary_of_metrics(gauteng) == {'mean': 26244.42,
#                                    'median': 24403.5,
#                                    'variance': 108160153.17,
#                                    'standard deviation': 10400.01,
#                                    'min': 8842.0,
#                                    'max': 39660.0}
#  ```

# In[1]:


def dictionary_of_metrics(items):

    mean = lambda data : sum(data)/len(data)
        
    maxim = lambda data : max(data)
    
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
               'standard deviation':stdv(data), 'min':minimum(data), 'max':maxim(data)}
    
    return met_dic


# # Function 2: Five Number Summary
# 
# Write a function which takes in a list of integers and returns a dictionary of the [five number summary.](https://www.statisticshowto.datasciencecentral.com/how-to-find-a-five-number-summary-in-statistics/) Answers should be rounded to the nearest second decimal.
# 
# _**Expected Output:**_
# 
# ```python
# 
# gauteng = [39660.0,
#             36024.0,
#             32127.0,
#             39488.0,
#             18422.0,
#             23532.0,
#             8842.0,
#             37416.0,
#             16156.0,
#             18730.0,
#             19261.0,
#             25275.0]
# 
# five_num_summ(gauteng) == {'max': 39660.0,
#                            'median': 24403.5,
#                            'min': 8842.0,
#                            'q1': 18422.5,
#                            'q3': 36024.5}
# 
# ```

# In[ ]:


def five_num_summ(items):
    ### Code Here
    pass


# # Function 3: Date Parser
# 
# Write a function which takes a list of datetime strings and converts it into a list of strings with only the date. 
# <br>
# <br>
# _**Expected Output:**_
# 
# ```python
# 
# dates = ['2019-11-29 12:50:54',
#          '2019-11-29 12:46:53',
#          '2019-11-29 12:46:10',
#          '2019-11-29 12:33:36',
#          '2019-11-29 12:17:43',
#          '2019-11-29 11:28:40']
# 
# date_parser(dates) == ['2019-11-29',
#                        '2019-11-29',
#                        '2019-11-29',
#                        '2019-11-29',
#                        '2019-11-29',
#                        '2019-11-29']
# 
# ```

# In[ ]:


def date_parser(list_dates):

  ### Code Here

  pass


# # Function 4: Municipality & Hashtag Remover
# 
# Write a function which takes in a pandas dataframe and returns the same dataframe which is modified. The function should do the following:
# 
# * Extract the municipality from a tweet using the dictonary given below into a new column in the same dataframe.
# * Extract the hashtag from a tweet into a new column in the same data frame.
# * The column headers should be "municipality" & "hashtags" respectively.
# * For those tweets which don't have the either a municipality nor a hashtag, fill it with ```np.nan```.
# 
# Note: Only pandas and numpy packages may be used.
# 
# ```python
# 
# municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
#             '@CityPowerJhb' : 'Johannesburg',
#             '@eThekwiniM' : 'eThekwini' ,
#             '@EMMInfo' : 'Ekurhuleni',
#             '@centlecutility' : 'Mangaung',
#             '@NMBmunicipality' : 'Nelson Mandela Bay',
#             '@CityTshwane' : 'Tshwane'}
# 
# ```

# _**Expected Outputs:**_ 
# 
# ```python
# 
# extract_municipality_hashtags(twitter_df).iloc[:11, :10]
# 
# ```
# ![image](https://github.com/RidhaMoosa/eskom_data-/blob/master/function4.png?raw=true)

# In[ ]:


def extract_municipality_hashtags(df):

  ### Code Here

  pass


# # Function 5: Number of Tweets per Day
# 
# Write a function which calculates the number of tweets that were posted per day. 
# 
# This function should take in a pandas dataframe and return a new dataframe with columns "```Date```" & "```Number of Tweets```"
# 
# Note: Only pandas and numpy may be used.
# 
# _**Expected Output:**_
# 
# ```python
# 
# number_of_tweets_per_day(twitter_df)
# 
# ```
# 
# ![function5](https://github.com/RidhaMoosa/eskom_data-/blob/master/function5.png?raw=True)

# In[ ]:


def number_of_tweets_per_day(df):

  ### Code Here

  pass


# # Function 6: Word Splitter
# 
# Write a function which splits a sentence into a list of the separate words. This is also known as [tokenization](https://www.geeksforgeeks.org/nlp-how-tokenizing-text-sentence-words-works/).
# 
# The function should take in a dataframe and return a data with a new column "```Split Tweets```". Words should also all be lowercase.
# 
# Note: Only pandas and numpy packages may be used.
# <br>
# <br>
# _**Expected Output**_:
# 
# ```python
# 
# word_spliter(twitter_df) 
# 
# ```
# 
# ![Function6](https://github.com/RidhaMoosa/eskom_data-/blob/master/Function6.png?raw=true)

# In[ ]:


def word_spliter(df):

  ### Code Here

  pass


# # Function 7: Stop Words & Link Remover
# 
# Write a function which removes the stop words and the ur link from a tweet. The function should follow the criteria below:
# 
# * Should remove stop words based on the dictionary provided below.
# * Should remove url's from the tweets. 
# * The function will also need to tokenise thee sentence as indicated in function 6. Note: Function 6 may not be called within this function.
# * The column should be labelled as "```Without Stop Words```"
# <br>
# <br>
# 
# ```python 
# stop_words_dict = {'stopwords':['where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 'may', 'why', '’s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 'their', 'various', 'thereafter', '‘d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', '’ve', 'might', 'see', 'whose', 'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 'became', 'however', 'many', 'thence', 'onto', '‘m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', '’d', 'under', 'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 'n’t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 'much', 'another', 'since', 'hundred', 'serious', '‘ve', 'ever', 'out', 'full', 'themselves', 'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', '’ll', 'latterly', 'are', 'ten', 'hers', 'should', 'they', '‘s', 'either', 'am', 'be', 'perhaps', '’re', 'only', 'namely', 'sixty', 'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', '‘ll', 'too', 'seems', '’m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'n‘t', 'him', 'could', 'front', 'within', '‘re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 'same', 'were', 'it', 'every', 'third', 'together']}
# ```
# <br>
# <br>
# 
# _**Expected Output**_:
# 
# ```python
# stop_words_http_remover(twitter_df)
# ```
# 
# ![function7](https://github.com/RidhaMoosa/eskom_data-/blob/master/Function7.png?raw=true)

# In[ ]:


def stop_words_http_remover(df):

  # Code Here

  pass

