# this module grabs content from reddit.com because we can build PRAW.Submission objects from post urls
# here is where we get those urls
# written by Matthew Trager, started 10/7/2017

from requests import get
from time import sleep
import re
from bs4 import BeautifulSoup

# soupify me captain!
def soupify(webpage):
    # get a post
    # TODO some sort of error checking here
    r = get(webpage)

    # get html from response
    # TODO can check for doctype=html format
    html = r.text

    # make me soup!
    # TODO some sort of error protection here
    soup =  BeautifulSoup(html, 'html.parser')
    return soup

# for reddit when there is only one <a> on the page, it means we were detected as a bot
# NOTE this is subject to change
def we_are_bot(soup):
    a_tags = []
    for tag in soup.find_all('a'):
        a_tags.append(tag)
    return len(a_tags) == 1

# always returns human soup (never bot soup)
def human_soup(webpage):
    soup = soupify(webpage)
    if we_are_bot(soup):
        print('botted, waiting 3s')
        sleep(3) # it is recommended to wait after getting detected as a bot (so says the bot soup)
        return human_soup(webpage)
    else:
        print('this is human soup boi')
        return soup

# gets all the urls for each post on the subreddit's web frontpage
def subreddit_frontpage(soup):
    # TODO error checking
    divs = soup('div', class_='entry')
    links = []
    prefix = 'https://www.reddit.com'
    for div in divs:
        tag = div.find('a')
        suffix = tag['href']
        # BUG have to prepend each url with this string:
        links.append(prefix + suffix)
    return links

# gets the number comments from visiting the live subreddit and sums the number of comments below each post's title
def get_num_web_comments(soup):
    num_comments = 0
    # NOTE target in a.bylink.comments.may-blank tag subject to change
    elements = soup('a', class_='comments')
    for element in elements:
        # # only want the integer from this, not all the text
        target = element.get_text()
        target = int(re.search(r'\d+', target).group()) # convert regex result to integer
        num_comments = num_comments + target
    return num_comments
