#!/usr/bin/python3

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer

#Tokenizing
sentence = "Jim is bringing his bulldog to eat at Friendlys?"
tokens = word_tokenize(sentence)
print (tokens)

#Removing Stop-words like 'is','his',etc.
stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if w not in stop_words]
print (tokens)

#Stemming
ps = LancasterStemmer()
for t in tokens:
    print (ps.stem(t))
