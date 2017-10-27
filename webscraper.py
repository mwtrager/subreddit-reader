# this module builds lists of text from reddit posts and comments
# written by Matthew Trager, started 10/7/2017

# imports
from requests import get
from bs4 import BeautifulSoup
import time # TODO do i need this else where still?

# BUG top 200 comments only. gotta dive deeper for all the comments
# TODO make it work even when the first post isn't a text post (could be pic or link elsewhere)
    # careful if it links to another reddit post

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
    soup = soupify(webpage)
    if we_are_bot(soup):
        print('botted waiting 3s')
        time.sleep(3)
        return human_soup(webpage)
    else:
        print('this is human soup boi')
        return soup

def get_post_divs(soup):
    # TODO get only the divs with posts in them
    # looks like a div with class entry is good NOTE if I make sure that I am indeed on a subreddit home page TODO
    # gotta then get all the a tags under that div but theres more than one a-tag there
    post_divs = soup('div', class_='entry')
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

# just get the title of the post from the frontpage
def get_post_titles(soup):
    # TODO error check that this is subreddit soup
    # TODO i want these available so I can use them when I reach out to the title's page
    titles = []
    [titles.append(tag.get_text()) for tag in soup('a', 'title')] # list of title text
    # print(titles)

    # get text from <a> w/ class title
    return titles
