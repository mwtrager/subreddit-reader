# take in a subreddit and perform analysis on each post

from webscraper import *
from processing import *
import time

# TODO I need to make this function production ready
# right now it's pretty basic
# I can be doing a lot more right here that would demonstrate
# the power of NLTK
# TODO I should build more functions in processing.py
# and use them here

# if we are bot, i have to send out a new request
# to get new soup

def perform(urls):
    for url in urls:
        print(url)
        print('getting the soup!')
        soup = human_soup(url)
        # get divs from soup
        print('getting appropriate divs...')
        divs = get_divs(soup)

        # get text from divs
        print('getting text from html...')
        text = get_raw(divs)

        # tokenize the text
        print('tokenizing the text...')
        tokenized_entries = tokenize(text)

        # combine all entries into one mess
        print('coagulation of tokens into one large list')
        words = get_words(tokenized_entries)

        # get vocab
        print('getting vocabulary...')
        vocab = get_vocab(words)

        # did anyone say lol?
        print('how many times did the word THE appear?')
        count = words.count('the')
        print(str(count) + ' times!')
        print('oh yea? well what percentage is that of the whole text?')
        percentage = 100 * count / len(words)
        percentage = round(percentage, 2)
        print(str(percentage) + '%!')
        print('hm. cool.')

        # calculate lexical diversity of this post!
        print('calculating lexical diversity...')
        print('lexical diversity is ' + str(lexical_diversity(words, vocab)))

        # ALL DONE
        print('sleep for 3 seconds to deter bot detection\n\n')
        time.sleep(3)





































        # if we_are_bot(soup):
        #     print('detected as bot :(')
        #     print('waiting 3 seconds...\n\n')
        #     time.sleep(3)
        # else:
        #     # get divs from soup
        #     print('getting appropriate divs...')
        #     divs = get_divs(soup)
        #
        #     # get text from divs
        #     print('getting text from html...')
        #     text = get_raw(divs)
        #
        #     # tokenize the text
        #     print('tokenizing the text...')
        #     tokenized_entries = tokenize(text)
        #
        #     # combine all entries into one mess
        #     print('coagulation of tokens into one large list')
        #     words = get_words(tokenized_entries)
        #
        #     # get vocab
        #     print('getting vocabulary...')
        #     vocab = get_vocab(words)
        #
        #     # did anyone say lol?
        #     print('how many times did the word THE appear?')
        #     count = words.count('the')
        #     print(str(count) + ' times!')
        #     print('oh yea? well what percentage is that of the whole text?')
        #     percentage = 100 * count / len(words)
        #     percentage = round(percentage, 2)
        #     print(str(percentage) + '%!')
        #     print('hm. cool.')
        #
        #     # calculate lexical diversity of this post!
        #     print('calculating lexical diversity...')
        #     print('lexical diversity is ' + str(lexical_diversity(words, vocab)))
        #
        #     # ALL DONE
        #     print('sleep for 3 seconds to deter bot detection\n\n')
        #     time.sleep(3)

    # TODO we gotta change this
    return 1

# TODO error checking needs to happen here
base_url = 'https://www.reddit.com/r/'
subreddit = input('Enter the name of a subreddit: ')

soup = human_soup(base_url + subreddit)
if we_are_bot(soup):
    print('detected as bot :(')
else:
    post_divs = get_post_divs(soup)
    post_links = get_post_links(post_divs)
    [print(link) for link in post_links]
    perform(post_links)
