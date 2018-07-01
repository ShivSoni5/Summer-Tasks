#!/usr/bin/python3

from nltk.corpus import wordnet

def syn_ant(word):
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            synonyms.append(lem.name())
            if lem.antonyms():
                antonyms.append(lem.antonyms()[0].name())
    return synonyms, antonyms

s, a = syn_ant('bulldog')
print(set(s))
print(set(a))
s, a = syn_ant('bull')
print(set(s))
print(set(a))
