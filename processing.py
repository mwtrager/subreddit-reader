# this module will do NLP using input from the webscraper
import nltk

def tokenize(entries):
    # TODO error check
    # BUG I'm getting garbage data from links and shit
    # NOTE This returns a list of comments, so using len(tokens) returns op + # of comments
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

    # -- NOTE
        # words has plurals in it
        # english_vocab does not

        # i need all words that don't appear in english_vocab
        # plurals don't appear in english_vocab, but they aren't "unusual"
        # therefore i want to replace the plural version of the word with singular
        # then check words against english_vocab
    # --

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

    return sorted(unusuals)
