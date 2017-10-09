# this program builds lists of words from comments on a given reddit post
# written by Matthew Trager, started 10/7/2017

# imports
from requests import get
from bs4 import BeautifulSoup as make_me_soup
import nltk

post = 'https://www.reddit.com/r/cscareerquestions/comments/751ylo/do_you_think_developers_should_be_shielded/'
print ('Building list from ' + post)

# get a post
r = get(post)

# get html from response
html = r.text

soup = make_me_soup(html, 'html.parser')

# when there is only one <a> on the page, it means we were detected as a bot
def we_are_bot():
    a_tags = []
    for tag in soup.find_all('a'):
        a_tags.append(tag)

    return len(a_tags) == 1

if we_are_bot():
    print('detected as bot :(')
else:
    # find all divs with class usertext-body
    divs = soup('div', class_='usertext-body')

    # ignore the first one because its garbage
    # TODO fix this
    divs = divs[1:]

    # tokenize comments
    comments_wordlists = []
    for div in divs:
        # use div.get_text to get all text of all children nodes to div.usertext-body
        text = div.get_text()
        tokens = nltk.word_tokenize(text)
        # print(tokens)
        comments_wordlists.append(tokens)

    # output for testing
    print('Length of comments_worldlist should be equal to comments on post + 1 (for OP)')
    print(len(comments_wordlists))
    
    print('printing OP')
    print(comments_wordlists[:1])

    print('printing first comment')
    print(comments_wordlists[1:2])
    
    print('print last comment')
    print(comments_wordlists[-1:])
