import nltk
import string
import random
import math
from math import log
from random import shuffle
from nltk.tokenize import sent_tokenize, word_tokenize


#********Processing True Reviews*********#
fp = open("hotelT-train.txt","r")
pos_file = fp.read()
vocab = 0
#Split into reviews
list_pos_reviews = pos_file.split()

count_pos=0
for i in list_pos_reviews :
       if 'ID-' in i:
           count_pos+=1
           list_pos_reviews.pop(list_pos_reviews.index(i))

string_pos_reviews = str(list_pos_reviews)
#removing punctuations
exclude = set(string.punctuation)
string_pos_reviews = ''.join(ch for ch in string_pos_reviews if ch not in exclude).lower()

#tokenizing into words:
list_pos_words =  (word_tokenize(string_pos_reviews))

str_pos_words = str(list_pos_words)

dict_pos_words = {}


for word in list_pos_words:
     word = word.lower()
     if word in dict_pos_words.keys():
        dict_pos_words[word] += 1
     else:
        dict_pos_words[word] = 1
        vocab += 1


pos_vocab = len(dict_pos_words)


total_pos_words = sum(dict_pos_words.values())

fp.close()



#***********Processing False reviews****************#

fn = open("hotelF-train.txt","r")
neg_file = fn.read()

list_neg_reviews = neg_file.split()

count_neg = 0
for i in list_neg_reviews :
    if "ID-" in i:
        count_neg+=1
        list_neg_reviews.pop(list_neg_reviews.index(i))

string_neg_reviews = str(list_neg_reviews)
#removing punctuations
exclude = set(string.punctuation)
string_neg_reviews = ''.join(ch for ch in string_neg_reviews if ch not in exclude).lower()

list_neg_words =  (word_tokenize(string_neg_reviews))

str_neg_words = str(list_neg_words)

dict_neg_words = {}

for w in list_neg_words:
     w = w.lower()
     if w not in dict_pos_words.keys() and w not in dict_neg_words.keys():
        vocab += 1
     if w in dict_neg_words.keys():
        dict_neg_words[w] += 1
     else:
        dict_neg_words[w] = 1

neg_vocab = len(dict_neg_words)

total_neg_words = sum(dict_neg_words.values())

fn.close()



fo = open("outputDD","w")


#NAIVE-BAYES-CLASSIFIER WITH LAPLACE SMOOTHING

for line in open("hotelDeceptionTest.txt"):
    pos_prob = math.log(count_pos)-math.log(count_pos+count_neg)
    neg_prob = math.log(count_neg)-math.log(count_pos+count_neg)
    tokens = line.split()
    ID = tokens.pop(0)
    exclude = set(string.punctuation)
    for token in tokens:
        token = ''.join(ch for ch in token if ch not in exclude)
        token = token.lower()
        if token in dict_pos_words.keys():
            pos_prob += (math.log(dict_pos_words[token] + 1)-math.log(total_pos_words + vocab))
        else:
            pos_prob += (-math.log(total_pos_words + vocab))

        if token in dict_neg_words.keys():
            neg_prob += (math.log(dict_neg_words[token] + 1)-math.log(total_neg_words + vocab))
        else:
            neg_prob += (-math.log(total_neg_words + vocab))


    if pos_prob > neg_prob:
        fo.write(ID + " T\n")

    else:
        fo.write(ID + " F\n")

fo.close()

import os
os.system(" python eval.py 1gold_file Banerjee_Sananda_extra_out")



