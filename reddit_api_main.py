import json
from pprint import pprint
import praw
from webscraper import *
from processing import *

# TODO do NOT commit this code into git without removing secrets from this file
    # must put in a git ignored file!!!
    # OR use as env variables on local machine

# TODO get the score of each comment and somehow maintain that association!

# get reddit
reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret,
                     user_agent=agent)
print('got reddit?', reddit.read_only)

# get all links on the front page for PRAW to make object from these submissions
soup = human_soup('https://www.reddit.com/r/jokes/')
divs = get_post_divs(soup)
links = get_post_links(divs)
print('Number of links being sent in:', len(links))

num_comments = 0
num_links = 0
for link in links:
    num_links = num_links + 1
    submission = reddit.submission(url=link)
    print('hitting submission:', submission.title, '   ...number', num_links, 'of', len(links))
    print('replacing more...')
    submission.comments.replace_more(limit=None)
    # build inputs for processing.py (cant send it praw.comment objects)
    comments_list = []
    for comment in submission.comments.list():
        num_comments = num_comments + 1
        comments_list.append(comment.body)
    # tokenize, wordize, and get vocab
    tokenized = tokenize(comments_list)
    wordized = get_words(tokenized)
    vocabbed = get_vocab(wordized)
    if len(vocabbed) > 0:
        print(unusual_words(vocabbed))
    lexical_score = 0
    if len(wordized) > 0:
        lexical_score = lexical_diversity(wordized, tokenized)
    print('number of unique words in this shit', len(vocabbed), 'out of a total of', len(wordized), 'words, so lexical score of', lexical_score)

print('\n...totals...')
print('# of links', num_links)
print('# of comments:', num_comments)
