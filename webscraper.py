# this program builds lists of words from comments on a given reddit post
# written by Matthew Trager, started 10/7/2017

# imports
from requests import get
from bs4 import BeautifulSoup as make_me_soup

# get a post
r = get('https://www.reddit.com/r/cscareerquestions/comments/751tqk/unsure_how_much_to_ask_for_after_school/')

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

    # build word lists from comments
    # TODO need nltk here
    comments_wordlists = []
    for div in divs:
        child = div.find('p')
        text = child.get_text()
        wordlist = text.split(' ')
        comments_wordlists.append(wordlist)

    print(comments_wordlists[:1])
