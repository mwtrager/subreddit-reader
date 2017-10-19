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
        print(unusual_words(vocab))
        print('\n\n')

    return 1

# -- START -- #
base_url = 'https://www.reddit.com/r/'
subreddit = input('enter a subreddit: ') # TODO error checking needs to happen here
sub_soup = human_soup(base_url + subreddit)
post_divs = get_post_divs(sub_soup)
post_links = get_post_links(post_divs)
test_unusual_words(post_links)
