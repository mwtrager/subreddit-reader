# this module will do NLP using input from the webscraper

import nltk

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

def singular(word):
    # BUG i would say possessives, but those are tokenized and aren't included?
        # STILL they type "shes" instead of "she's" and "shes" will get transformed to "sh"

    # words ending in 'ies'
    if word.endswith('ies'):
        return word[:-3] + 'y'

    # words ending in 'es'
    elif word[-2:] in ['es']:
        # BUG words that are singular ending in e should just remove the s
            # NOTE take away the es
                # if it can't pluralise to end in 'es' then it is a "singular ending in e" plural
                # this doesnt work though w/ "aches" like in "headaches" and other similar words
                    # list of valid words that end like this
                    # [word for word in english if wword.endswith('che')]
                        # this is a small list maybe it's a good idea to check against it
                    # luckily 'she' is the only word in english that ends in 'she'
                # NOTE UGH what about [w for w in english if w.endswith('ches')] breeches, riches
                # NOTE UGH theres even [w for w in english if w.endswith('shes')] ashes, brushes, +3 others
        test = word[:-2]
        if not plural(test) in [word]:
            # it can't pluralize to end in 'es' therefore it's a singular ending in e NOTE not necessarily
            # just remove the s
            return word[:-1]
        else:
            return word[:-2]

    # words ending in 'en'
    elif word.endswith('en'):
        return word[:-2] + 'an'

    # words ending in 's'
    else:
        return word[:-1]

def unusual_words(words):
    english = set(word.lower() for word in nltk.corpus.words.words())
    unusuals = []
    for word in words:
        # BUG galore singularizing words that may not need it?
        if word not in english:
            if singular(word) not in english:
                unusuals.append(word)

    return sorted(unusuals)
