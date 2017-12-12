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
print('got reddit?', reddit.read_only)

soup = human_soup('https://www.reddit.com/r/'+subreddit+'/')
links = subreddit_frontpage(soup)
print('Number of links being sent in:', len(links))

# count the total number of comments from hitting the web to compare with api
num_web_comments = get_num_web_comments(soup)

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
print('# of api comments:', num_comments)
print('# of web comments:', num_web_comments)
print('a difference of', num_comments-num_web_comments, 'comments')
