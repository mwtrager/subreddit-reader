# this module builds lists of text from reddit posts and comments
# written by Matthew Trager, started 10/7/2017

# imports
from requests import get
from bs4 import BeautifulSoup
import time # TODO do i need this else where still?

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

# always returns human soup (never bot soup)
def human_soup(webpage):
    # soupify
        # not human soup? return human_soup(soupify(webpage))
        # human soup? return soup
    soup = soupify(webpage)
    if we_are_bot(soup):
        print('botted waiting 3s')
        time.sleep(3)
        return human_soup(webpage)
    else:
        return soup

    # # TODO make a function that will always return human soup based on we_are_bot
    # if we_are_bot(soup):
    #     new_soup = soupify(webpage)
    #     return human_soup(webpage, new_soup) # NOTE this might be retarded
    # else:
    #     return soup

def get_post_divs(soup):
    # TODO get only the divs with posts in them
    # looks like a div with class entry is good NOTE if I make sure that I am indeed on a subreddit home page TODO
    # gotta then get all the a tags under that div but theres more than one a-tag there
    post_divs = soup.find_all('div', class_='entry')
    return post_divs

def get_post_links(post_divs):
    # TODO error checking?
    # NOTE i can't belive this works!
    post_links = []
    prefix = 'https://www.reddit.com'
    for post_div in post_divs:
        tag = post_div.find('a')
        suffix = tag['href']
        # BUG have to prepend each url with this string:
        post_links.append(prefix + suffix)
    return post_links

# okay lets say i have a list of a_tags...
# next move, go through each a_tag and perform what is in main...

# get the divs from the soup that we need
def get_divs(soup):
    divs = soup.find_all('div', class_='usertext-body')
    # HACK ignore divs[0] first one because it's the sidebar
    divs = divs[1:]
    return divs

def get_raw(divs):
    # TODO error check
    # BUG I'm getting some garbage data with links and whatever
        # how to avoid?
    return [div.get_text() for div in divs]
