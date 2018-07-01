#!/usr/bin/python3

from nltk.corpus import wordnet

w1 = wordnet.synset('bulldog.n.01')
w2 = wordnet.synset('poodle.n.01')
print (w1.wup_similarity(w2))

w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))

w2 = wordnet.synset('space.n.01')
print(w1.wup_similarity(w2))

w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))
