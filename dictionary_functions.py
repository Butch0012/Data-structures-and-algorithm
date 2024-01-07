import string

def word_frequency(sentence):
     words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()