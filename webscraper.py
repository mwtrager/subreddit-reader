# this program builds lists of words from comments on a given reddit post
# written by Matthew Trager, started 10/7/2017

# imports
from requests import get
from bs4 import BeautifulSoup
import nltk

def soupify(webpage):
    # get a post
    # TODO some sort of error checking here
    r = get(webpage)

    # get html from response
    # TODO can check for doctype=html formatt
    html = r.text

    # make me soup!
    # TODO some sort of error protection here
    soup =  BeautifulSoup(html, 'html.parser')
    return soup

# for reddit when there is only one <a> on the page, it means we were detected as a bot
def we_are_bot(soup):
    a_tags = []
    for tag in soup.find_all('a'):
        a_tags.append(tag)

    return len(a_tags) == 1

# filter the soup, get the text, tokenize with nltk
def get_posts_tokenized(soup):
    # find all divs with class usertext-body
    divs = soup('div', class_='usertext-body')

    # HACK ignore the first one because its the sidebar
    divs = divs[1:]

    # tokenize comments
    posts_tokenized = []
    for div in divs:
        # use div.get_text to get all text of all children nodes to div.usertext-body
        text = div.get_text()
        tokens = nltk.word_tokenize(text)
        # print(tokens)
        posts_tokenized.append(tokens)

    return posts_tokenized

def get_comments_text(soup):
    # TODO maybe
    return comments_text

def get_op(posts):
    # TODO error check
    op = posts[0]
    return op

def get_comments(posts):
    # TODO error check
    comments = posts[1:]

def get_reddit_posts(url):
    soup = soupify(url)

    # TODO how do we do proper returns?
    if we_are_bot(soup):
        return []
    else:
        # TODO error checking to make sure it's a reddit POST and not any other reddit page
        posts = get_posts_tokenized(soup)
        return posts

# TODO rename and fix
# BUG using isalpha ignores some data like if someone typed '9gag' maybe
# i want this to return unique words contained from this entire page
# right now it returns the vocab of each post
def get_vocab_from_posts(posts):
    # put all words into same list to make this easier
    all_words = []

    # so for each post, append words to all_words
    for post in posts:
        all_words.append([word.lower() for word in post if word.isalpha()]) # BUG it still returns a list of lists!
        # vocab = sorted(set(words))
        # post_vocabs.append(vocab)

    # print(all_words)
    return post_vocabs
