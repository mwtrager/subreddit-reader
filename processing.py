# this module will do NLP using input from the webscraper
import nltk

def tokenize(entries):
    # TODO error check
    # how to handle links that people put in?
    # BUG I'm getting garbage data from links and shit
    return [nltk.word_tokenize(entry) for entry in entries]

# TODO rename and fix
# BUG using isalpha ignores some data like if someone typed '9gag' maybe
# returns unique words used in the whole reddit post
def get_vocab(entries):
    # put all words into same list to make this easier
    entry_words = []
    all_words = []
    # so for each entry, append words to entry_words
    for entry in entries:
        entry_words.append([word.lower() for word in entry if word.isalpha()])
        [all_words.append(word) for entry in entry_words for word in entry] # list comprehension. is this coshure?
        # TODO need a function to return all_words so that I can easily calculate lexical diversity
        vocab = sorted(set(all_words))
    return vocab

# def stress(pron):
# ...     return [char for phone in pron for char in phone if char.isdigit()]


# get vocab
# [page_vocab.append(word) for entry in all_words for word in entry]
