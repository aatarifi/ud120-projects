# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:39:24 2018

@author: Ahmad
"""
import nltk
from nltk.corpus import stopwords
sw = stopwords.words("english")
sw[0]
len(sw)
stopwords_count = set(stopwords.words("english"))
len(stopwords_count)
stopwords_count
stopwords.fileids()

sw_a = stopwords.words("spanish")
sw[0]
set(stopwords.words("spanish"))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
import nltk
from nltk.stem.snowball import SnowballStemmer
import string
words = "Hi Everyone  If you can read this message youre properly using parseOutText  Please proceed to the next part of the project"

stemmer = SnowballStemmer("english")
stemmer.stem("Hi")
        
words_list = words.split()
print words_list
togother = []
for i in words_list:
  j = stemmer.stem(i)
  togother.append(j) 
togother = ' '.join(togother)

print togother
            
#            stemed_word = stemmer.stem(i)
#            #full_words = words_list.append(stemed_word)
#            makeitastring = ''.join(stemed_word)
#     
#        words = makeitastring