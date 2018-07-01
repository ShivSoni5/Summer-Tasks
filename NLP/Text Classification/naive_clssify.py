#!/usr/bin/python3

from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

training_data = []
training_data.append({"class":"greeting", "sentence":"how are you?"})
training_data.append({"class":"greeting", "sentence":"how is your day?"})
training_data.append({"class":"greeting", "sentence":"good day"})
training_data.append({"class":"greeting", "sentence":"how is it going today?"})

training_data.append({"class":"goodbye", "sentence":"have a nice day"})
training_data.append({"class":"goodbye", "sentence":"see you later"})
training_data.append({"class":"goodbye", "sentence":"have a nice day"})
training_data.append({"class":"goodbye", "sentence":"talk to you soon"})

training_data.append({"class":"sandwich", "sentence":"make me a sandwich"})
training_data.append({"class":"sandwich", "sentence":"can you make a sandwich?"})
training_data.append({"class":"sandwich", "sentence":"having a sandwich today?"})
training_data.append({"class":"sandwich", "sentence":"what's for lunch?"})
#print (f"{len(training_data)} sentences of training data")

corpus_words = {}
class_words = {}

classes = list(set([a['class'] for a in training_data]))
#print (classes)

for c in classes:
    # prepare a list of words within each class
    class_words[c] = []

# loop through each sentence in our traning data
for data in training_data:
    for word in word_tokenize(data['sentence']):
        if word not in ["?", "'s"]:
            stemmed_word = stemmer.stem(word.lower())
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            class_words[data['class']].extend([stemmed_word])

#print (f'Cospus words and counts: {corpus_words}\n')
#print (f'Class words: {class_words}')

def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    for word in word_tokenize(sentence):
        if stemmer.stem(word.lower()) in class_words[class_name]:
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                print (f"  match: {stemmer.stem(word.lower())} ({1/corpus_words[stemmer.stem(word.lower())]})")

    return score

'''
sentence = "good day for us to have lunch?"

for c in class_words.keys():
    print (f'Class: {c} Score: {calculate_class_score(sentence, c)}\n')
'''

def classify(sentence):
    high_class = None
    high_score = 0

    for c in class_words.keys():
        score = calculate_class_score(sentence, c, show_details=False)
        if score > high_score:
            high_class, high_score = c, score

    return high_class, high_score

if __name__ == '__main__':
    print(classify('make me some lunch?'))
    print(classify('sudo make me a sandwich'))
    print(classify('take care'))
    print(classify('talk to you later'))
    print(classify('who are you'))
    print(classify('am i crazy?'))
