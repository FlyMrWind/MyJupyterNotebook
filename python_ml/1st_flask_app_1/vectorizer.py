# -*- coding: utf-8 -*-
# @Author: hsz
# @Date:   2019-07-11 17:31:32
# @Last Modified by:   hsz
# @Last Modified time: 2019-07-11 17:49:16

from sklearn.feature_extraction.text import HashingVectorizer
import re 
import os
import pickle

cur_dir = os.path.dirname(__file__)
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl'), 'rb'))

def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

vect = HashingVectorizer(decode_error='ignore', n_features=2**21, preprocessor=None, tokenizer=tokenizer)
