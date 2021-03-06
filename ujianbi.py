# -*- coding: utf-8 -*-
"""ujianBI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wIlInYu2wBqeo_IUKqSPrkFjTJJjw4ua
"""

import numpy as np
import csv
import pandas as pd

import tweepy
import re
from textblob import TextBlob

access_token= "252355250-WRVNehrYcE5qGDcLxRhAPk0CnDMuqW97YzhHVXft"
access_token_secret= "qgEkn7rIXGrtfNH480f57sxt6eEhQN5yxVTM0GLcMrPTk"
api_key= "NZJNThB5NHwSvzW6iw7n4XVaL"
api_key_secret= "IVKEFZCe6weYt4Xev6Ws25rfynxd9VhV6qDltcGgLYZtwzGrdX"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

hasilSearch = api.search(q="indosat", lang="en", count=100)

hasilAnalisis = []

for tweet in hasilSearch:
    tweet_properties = {}
    tweet_properties["Tanggal_tweet"] = tweet.created_at
    tweet_properties["Pengguna"] = tweet.user.screen_name
    tweet_properties["Isi_tweet"] = tweet.text
    tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
  
      
    analysis = TextBlob(tweet_bersih)
    
    if analysis.sentiment.polarity > 0.0:
        tweet_properties["Sentiment"] = "Positif"
    elif analysis.sentiment.polarity == 0.0:
        tweet_properties["Sentiment"] = "Netral"
    else:
        tweet_properties["Sentiment"] = "Negatif"

    if tweet.retweet_count >0:
        if tweet_properties not in hasilAnalisis:
            hasilAnalisis.append(tweet_properties)
    else :
        hasilAnalisis.append(tweet_properties)

tweet_positif = [t for t in hasilAnalisis if t["Sentiment"]=="Positif"]
tweet_netral = [t for t in hasilAnalisis if t["Sentiment"]=="Netral"]
tweet_negatif = [t for t in hasilAnalisis if t["Sentiment"]=="Negatif"]
print(tweet_negatif)

print("hasilAnalisis")
print("Positif: ", len(tweet_positif), "({}%)".format(100*len(tweet_positif)/len(hasilAnalisis)))
print("Netral: ", len(tweet_netral), "({}%)".format(100*len(tweet_netral)/len(hasilAnalisis)))
print("Negatif: ", len(tweet_negatif), "({}%)".format(100*len(tweet_negatif)/len(hasilAnalisis)))