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

def plural(word):
    if word.endswith('y'):
        return word [:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def singular(word):
    # mirror image of plural
    if word.endswith('ies'):
        return word[:-3] + 'y'
    elif word[-2:] in ['es']:
        return word[:-2]
    elif word.endswith('en'):
        return word[:-2] + 'an'
    else: # ends in 's'
        return word[:-1]

# cleanup in aisle 2...
def unusual_words(words):
    # BUG getting normal words still, blame plural() i think?
    # NOTE this is the stopping point as far as adding processing logic to this branch!!!!
        # I really shouldn't even be adding this in, but it's too late and too fun!
    # BUG hey listen! nltk english vocab does NOT include plurals

    # -- NOTE
        # words has plurals in it
        # english_vocab does not

        # i need all words that don't appear in english_vocab
        # plurals don't appear in english_vocab, but they aren't "unusual"
        # therefore i want to replace the plural version of the word with singular
        # then check words against english_vocab
    # --


    # TODO  for word in words:
    # if word is not in english_vocab
    # if singular word is not in english_vocab
        # good.





    # NOTE NOTE NOTE NOTE
    # BINGO BANGO
    # I need a smaller dataset to dive into what's making it here and what isn't
    # Mostly to debug plural and singular functions
    # And the future tense-sensing-functions
    usuals = set(word.lower() for word in nltk.corpus.words.words())
    unusuals = []
    for word in words:
        if word not in usuals:
            if singular(word) not in usuals:
                unusuals.append(word)


    # words is lowercase alphabetic words
    # TODO if word or plural(word) is in words, don't return it
    # for word in words:
    #     if not word or plural(word) in words:
    #         unusuals.append(word)

    # pluralise every word in words and add it to words
    # then get difference?
    # plurals = []
    # [plurals.append(plural(word)) for word in words]
    # plurals = set(plurals)
    #
    # unusuals = words - usuals # NOTE this words...
    # unusuals = plurals - usuals
    return sorted(unusuals)
# def stress(pron):
# ...     return [char for phone in pron for char in phone if char.isdigit()]


# get vocab
# [page_vocab.append(word) for entry in all_words for word in entry]
