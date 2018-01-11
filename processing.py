import nltk

# build set of english words (only used in unusual_words() but i don't want to build it every time I call that)
english = set(word.lower() for word in nltk.corpus.words.words())

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

# return words that are not in the nltk english dictionary
def unusual_words(lemmas):
    unusuals = []
    for lemma in lemmas:
        if lemma not in english:
            unusuals.append(lemma)
    return sorted(unusuals)

def lemmatize(words):
    # NOTE gotta do some mort testing but it seems WNL produces less unusual words than Porter/Lancaster stemmers
    wnl = nltk.WordNetLemmatizer()
    return [wnl.lemmatize(word) for word in words]
