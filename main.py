# take in a subreddit and perform analysis on each post

from webscraper import *
from processing import *

# NOTE
# currently testing unusual_words!
def test_unusual_words(urls):
    # i want to get all the unusal words from each url in urls
    for url in urls:
        print('trying to get ' + url)
        soup = human_soup(url)
        divs = get_divs(soup)
        text = get_raw(divs)
        comments = tokenize(text)
        print('number of comments: ' + str(len(comments)))
        words = get_words(comments)
        vocab = get_vocab(words)
        target = unusual_words(vocab)
        print('lexical diversity: ' + str(lexical_diversity(words, vocab)))
        print('number of unusual words: ' + str(len(target)))
        print(target)
        print('\n\n')

    return 1

# -- START -- #
print('get all unusual words from all the posts on a subreddits frontpage')
base_url = 'https://www.reddit.com/r/'
subreddit = input('enter a subreddit: ') # TODO error checking needs to happen here
sub_soup = human_soup(base_url + subreddit)
titles = get_post_titles(sub_soup)

# TODO use these titles to give an overview of posts that will be ripped
    # and at the head of each loop so you give a good title
print('\n')
print('Posts to be ripped from', subreddit, '\n')
[print(title) for title in titles]

# post_divs = get_post_divs(sub_soup)
# post_links = get_post_links(post_divs)
# test_unusual_words(post_links)
