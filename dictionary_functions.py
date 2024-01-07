# File: dictionary_functions.py

import string

def word_frequency(sentence):
    # Convert the sentence to lowercase and remove punctuation
    words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()
    
    # Dictionary to store word frequencies
    frequency_dict = {}

    # Iterate through the words in the sentence
    for word in words:
        # Update the frequency of each word in the dictionary
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
# Return the final word frequency dictionary
    return frequency_dict
    
