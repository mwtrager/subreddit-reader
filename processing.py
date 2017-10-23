# this module will do NLP using input from the webscraper

import nltk

# build set of english words
english = set(word.lower() for word in nltk.corpus.words.words())
# build possible singulars once yep
possible_singulars_es = [word for word in english if (word.endswith('shes') or word.endswith('ches')) ]
possible_singulars_ies = [word for word in english if (word.endswith('ies') or word.endswith('ie'))]
possible_singulars_ens = [word for word in english if word.endswith('en')]

def tokenize(entries):
    # TODO error check
    # BUG I'm getting garbage data from links and shit
    # NOTE This returns a list of comments, so using len(comments) returns op + # of comments
    return [nltk.word_tokenize(entry) for entry in entries]

def get_words(entries):
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

# TODO observe the order of the if statements and choose most efficient order
# BUG words ending in 'ens' aren't accounted for
def singular(word):
    # words ending in 'ies'
    if word.endswith('ies'):
        # first check if the unchanged word is in possible_singulars_ies
        if word in possible_singulars_ies:
            return word
        # then check if the word minus s in in possible_singulars_ies
        elif word[:-1] in possible_singulars_ies:
            return word[:-1]
        # NOTE do i need the pluralization test
        # otherwise switch to y
        else:
            return word[:-3] + 'y'

    # words ending in 'es'
    elif word.endswith('es'):
        # first check if the unchanged word is in possible_singulars_es
        if word in possible_singulars_es:
            return word
        # then check if the word minus s is in possible_singulars_es MAYBE
        elif word[:-1] in possible_singulars_es:
            return word[:-1]
        # then do the pluralization test
        elif not plural(word[:-2]) in [word]:
            # it can't pluralize to end in 'es' therefore it's a singular ending in e NOTE not necessarily
            return word[:-1]
        # otherwise just return minus 'es'
        else:
            return word[:-2]

    # words ending in 'en'
    elif word.endswith('en'):
        if word in possible_singulars_en:
            return word
        return word[:-2] + 'an'

    # words ending in 's'
    elif word.endswith('s'):
        # BUG difficulty: high... singular('ashess') returns 'ashes'
        return word[:-1]

    # NOTE catch all -- might not need
    else:
        return word

# TODO and the number of times they appear
def unusual_words(words):
    unusuals = []
    for word in words:
        # BUG galore singularizing words that may not need it?
        if word not in english:
            if singular(word) not in english:
                unusuals.append(word)

    return sorted(unusuals)
