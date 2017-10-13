# this module builds lists of text from reddit posts and comments
# written by Matthew Trager, started 10/7/2017

# imports
from requests import get
from bs4 import BeautifulSoup

# -- PUBLIC -- #

def get_reddit_posts(url):
    soup = soupify(url)

    # TODO how do we do proper returns?
    if we_are_bot(soup):
        return []
    else:
        # TODO error checking to make sure it's a reddit POST and not any other reddit page
        posts = get_posts_tokenized(soup)
        return posts

# -- PRIVATE -- #

def soupify(webpage):
    # get a post
    # TODO some sort of error checking here
    r = get(webpage)

    # get html from response
    # TODO can check for doctype=html formatt
    html = r.text

    # make me soup!
    # TODO some sort of error protection here
    soup =  BeautifulSoup(html, 'html.parser')
    return soup

# for reddit when there is only one <a> on the page, it means we were detected as a bot
def we_are_bot(soup):
    a_tags = []
    for tag in soup.find_all('a'):
        a_tags.append(tag)

    return len(a_tags) == 1

# get the divs from the soup that we need
def get_divs(soup):
    divs = soup('div', class_='usertext-body')
    # HACK ignore divs[0] first one because it's the sidebar
    divs = divs[1:]
    return divs

def get_raw(divs):
    # TODO error check
    # BUG I'm getting some garbage data with links and whatever
        # how to avoid?
    return [div.get_text() for div in divs]
