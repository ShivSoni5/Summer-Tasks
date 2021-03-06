#!/usr/bin/python3

from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

sentence = "Jim is bringing his bulldog to eat at Friendlys?" 

#chunk the sentence
ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))

# IOB transform
# B-{CHUNK_TYPE} – for the word in the Beginning chunk
# I-{CHUNK_TYPE} – for words Inside the chunk
# O – Outside any chunk

iob_tagged = tree2conlltags(ne_tree)
print (iob_tagged)
print ([i for i in iob_tagged if i[2]=='B-ORGANIZATION'])
