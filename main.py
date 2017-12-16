import praw
from webscraper import *
from processing import *

# TODO get the score of each comment and somehow maintain that association!

# get all links on the front page for PRAW to make object from these submissions
# TODO error checking
subreddit = input('enter a subreddit: ')

# get reddit
reddit = praw.Reddit(client_id='',
client_secret='',
user_agent='')

soup = human_soup('https://www.reddit.com/r/'+subreddit+'/')
posts = subreddit_frontpage(soup)
print('Number of posts being sent in:', len(posts))

# IDEA i could use vocab as a set and search for certain words!

for post in posts[:1]:
    post = reddit.submission(url=post)
    print(post.title)
    post.comments.replace_more(limit=1)
    # TODO build these lists on the subreddit level
    raw_list = []
    tokens_list = []
    words_list = []
    vocab_list = []
    lemmas_list = []
    unusuals_list = []
    for comment in post.comments:
        raw = comment.body
        tokens = tokenize(raw)
        words = get_words(tokens)
        vocab = get_vocab(words)
        lemmas = lemmatize(sorted(vocab)) # NOTE sorted turns this to a list
        unusuals = unusual_words2(lemmas)

        raw_list.append(raw)
        tokens_list.append(tokens)
        words_list.append(words)
        vocab_list.append(vocab)
        lemmas_list.append(lemmas)
        if len(unusuals) > 0:
            unusuals_list.append(unusuals)

    print(len(unusuals_list))
