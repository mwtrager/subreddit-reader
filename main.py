# run me!

from webscraper import *
from processing import *

# for url in urls:
    # do everything in this file
    # how do i get such urls?
    # we_are_bot !!!!! it gets all the a-tags on a page...
    # steal that logic and build out a function
    # that will take in a subreddit and give all post urls as output
    # pass it to this code below and then i will be
    # doing this for each post on that subreddits front page

url = 'https://www.reddit.com/r/cscareerquestions/comments/75ldnr/thank_you/'

print('getting the soup!')
soup = soupify(url)

if we_are_bot(soup):
    print('detected as bot :(')
else:
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
