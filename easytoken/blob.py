import sys
import json

import nltk

import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 


class Partsofspeech():

    def pos(txt):
        tokens = nltk.word_tokenize(txt)
        return (nltk.pos_tag(tokens))
        # stop_words = set(stopwords.words('english'))