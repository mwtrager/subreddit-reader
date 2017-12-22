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
[print(post) for post in posts]
num_web_comments = get_num_web_comments(soup)

# IDEA i could use vocab as a set and search for certain words!

num_api_comments = 0
num_posts = 0
unusuals_list = []
for post in posts:
    num_posts = num_posts + 1
    post = reddit.submission(url=post) # BUG on posts that are outbound links
    print(post.title)
    post.comments.replace_more(limit=None)
    # TODO build these lists on the subreddit level
    raw_list = []
    tokens_list = []
    words_list = []
    vocab_list = []
    lemmas_list = []
    for comment in post.comments.list():
        num_api_comments = num_api_comments + 1
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

# flatten list
unusuals_list = [item for sublist in unusuals_list for item in sublist]
print(sorted(set(unusuals_list)))
print('number of posts being sent in:', len(posts))
print('number of posts processed:', num_posts)
print('number of api comments', num_api_comments)
print('number of web comments', num_web_comments)
