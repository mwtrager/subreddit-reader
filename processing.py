# this module will do NLP using input from the webscraper
import nltk

def tokenize(entries):
    # TODO error check
    # BUG I'm getting garbage data from links and shit
    # NOTE This returns a list of comments, so using len(tokens) returns op + # of comments
    return [nltk.word_tokenize(entry) for entry in entries]

def get_words(entries):
    # TODO change variable name? tokens is a little ambiguous...
    # BUG using isalpha ignores some data like if someone typed '9gag' maybe
    all_words = []
    entry_words = []
    for entry in entries:
        entry_words.append([word.lower() for word in entry if word.isalpha()])
        [all_words.append(word) for entry in entry_words for word in entry] # list comprehension. is this koshur?
    return all_words

def get_vocab(words):
    return set(words)

def lexical_diversity(words, vocab):
    return len(vocab)/len(words)

# def stress(pron):
# ...     return [char for phone in pron for char in phone if char.isdigit()]


# get vocab
# [page_vocab.append(word) for entry in all_words for word in entry]
