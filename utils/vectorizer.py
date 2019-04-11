import numpy as np
import os
import nltk
import gensim
import string
from gensim.models import Word2Vec
import utils.crawler as crawler
from nltk.corpus import stopwords

def vectorize_user(model, screen_name, limit=0):
    tweet_list = crawler.get_user_timeline(screen_name, limit=limit)
    tweet_vectors=[]
    for tweet in tweet_list:
        tv=vectorize_tweet(model, tweet.text)
        tweet_vectors.append(tv)
    return np.sum(tweet_vectors,axis=0)

def vectorize_tweet(model, tweet):
    word_vectors = []
    stop = stopwords.words('english')+list(string.punctuation)+list(string.digits)
    for word in nltk.tokenize.word_tokenize(tweet):
        if word.lower() not in stop:
            wv=model.wv[word.lower()]
            word_vectors.append(wv)
    return np.sum(word_vectors,axis=0)

