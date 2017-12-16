# this module handles natural language processing

import nltk

# lemmatization is to build a lemma from a word
    # eg. running --> run (run is a lemma, running is not)
# nltk has more than one stemmer available... choose one
# nltk.WordNetLemmatizer() might be my best choice because according to the book
    # it will always produce a valid list of lexicon headwords (words in the dictionary aka valid lemmas)
    # the downside is that it takes longer because of extra processing

# build set of english words
english = set(word.lower() for word in nltk.corpus.words.words())
# build possible singulars once
possible_singulars_es = [word for word in english if (word.endswith('shes') or word.endswith('ches'))]
possible_singulars_ies = [word for word in english if (word.endswith('ies') or word.endswith('ie'))]
possible_singulars_ens = [word for word in english if (word.endswith('en') or word.endswith('ens'))]

def tokenize(entry):
    # TODO error checking
    # BUG links come in here and they are bad data points
    return nltk.word_tokenize(entry)

def get_words(tokens):
    # BUG using isalpha ignores some data like if someone typed '9gag' maybe
    return [word.lower() for word in tokens if word.isalpha()]

def get_vocab(words):
    return set(words) # NOTE this returns a SET

def lexical_diversity(words, vocab):
    # BUG division by zero error! haha finally got one :(
    return len(vocab)/len(words)

# pluralizes a word (has bugs but i don't use this yet)
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

    # words ending in 'ens'
    elif word.endswith('ens'):
        # first check if the unchanged word is in possible_singulars_ens
        if word in possible_singulars_ens:
            return word
        # then check if the word minus s is in possible_singulars_ens
        elif word[:-1] in possible_singulars_ens:
            return word[:-1]

    # words ending in 'en'
    elif word.endswith('en'):
        # return it if it's already singular
        if word in possible_singulars_ens:
            return word
        # if it's not singular return it in singular form
        return word[:-2] + 'an'

    # words ending in 's'
    elif word.endswith('s'):
        # BUG difficulty: high... singular('ashess') returns 'ashes'
        return word[:-1]

    # NOTE catch all -- might not need
    else:
        return word

# return words that are not in the nltk english dictionary
def unusual_words(words):
    unusuals = []
    for word in words:
        if word not in english:
            if singular(word) not in english:
                unusuals.append(word)
    return sorted(unusuals)

# return words that are not in the nltk english dictionary
def unusual_words2(lemmas):
    # i dont thinks this works
    unusuals = []
    for lemma in lemmas:
        if lemma not in english:
            unusuals.append(lemma)
    return sorted(unusuals)

# TODO lets make a function that can deal the verb issue
    # ie: "running" is not an unusual word but i report it as such

def lemmatize(words):
    # NOTE gotta do some mort testing but it seems WNL produces less unusual words than Porter/Lancaster stemmers
    wnl = nltk.WordNetLemmatizer()
    return [wnl.lemmatize(word) for word in words]
