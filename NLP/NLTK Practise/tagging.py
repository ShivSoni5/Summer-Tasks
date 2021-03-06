#!/usr/bin/python3

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
from nltk import pos_tag
from string import punctuation

#Tokenizing
sentence = "Jim is bringing his bulldog to eat at Friendlys?"
tokens = word_tokenize(sentence)
print (tokens)

#Removing Stop-words like 'is','his' and pucntuations.
stop_words = set(stopwords.words('english'))
all_stop_words = stop_words | set(punctuation)  # bitwise OR in stop words and punctuation marks
tokens = [w for w in tokens if w not in all_stop_words]
print (tokens)

#Stemming
ps = LancasterStemmer()
for t in tokens:
    print (ps.stem(t))

#tagging
tags = pos_tag(tokens)
print (tags, "\nNouns: ", [t for t in tags if t[1] == "NN"])
