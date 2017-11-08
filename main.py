# take in a subreddit and perform analysis on each post

from webscraper import *
from processing import *
from time import sleep

# NOTE
# currently testing unusual_words!
def test_unusual_words(urls):
    # i want to get all the unusal words from each url in urls
    for url in urls:
        print('trying to get ' + url)
        url = url + '?limit=500' # 500 comments instead of 200 (hard limit) NOTE should i just put this here?
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

# TODO change the name ya dingus
def test_stuff(urls):
    # i want to get all the unusal words from each url in urls
    for url in urls:
        print('trying to get ' + url)
        soup = human_soup(url)
        print('----')
        print('')
        title = get_post_titles(soup)[0]
        divs = get_divs(soup)
        text = get_raw(divs)
        print(title)
        print('')
        print(text[0])
    return 1

# NOTE NOTE NOTE BEGIN THE ULTIMATE TEST

print('\n COUNT COMMENTS BEFORE WEBDRIVING\n')
# count comments normally with souping
print('requesting reddit page...')
soup = human_soup('https://www.reddit.com/r/AskReddit/comments/7aj2ek/what_over_1000_item_did_you_buy_and_did_not/')
divs = get_divs(soup)
text = get_raw(divs)
comments = tokenize(text)
print('number of comments: ' + str(len(comments)))
print('print last comment:')
print(comments[-1])

print('\n START WEBDRIVING\n')

print('import webdriver...')
from selenium import webdriver

print('creating headless driver with PhantomJS...')
driver = webdriver.PhantomJS()

print('requesting reddit page...')
driver.get('https://www.reddit.com/r/AskReddit/comments/7aj2ek/what_over_1000_item_did_you_buy_and_did_not/')
print('currently have', driver.current_url)

print('finding final span w/ classname morecomments...')
spans = driver.find_elements_by_class_name('morecomments')
if len(spans) > 1:
    button = spans[-1].find_elements_by_css_selector('*')[0]
    print('clicking:', button)
    driver.execute_script('arguments[0].click()', button)

# now that i've clicked, try to see if i got more comments after waiting

# wait
seconds = 3
print('waiting', seconds, 'seconds...')
sleep(seconds)

# import bs4
from bs4 import BeautifulSoup

# soupify driver.page_source
soup = BeautifulSoup(driver.page_source, 'html.parser')

# count comments normally with souping
divs = get_divs(soup)
text = get_raw(divs)
comments = tokenize(text)
print('number of comments: ' + str(len(comments)))
print('print last comment:')
print(comments[-1])

# BUG it returns the same amount of comments after the click on the span

driver.quit()

# -- START -- #
# print('get some jokes atm')
# base_url = 'https://www.reddit.com/r/'
# subreddit = input('enter a subreddit: ') # TODO error checking needs to happen here
# sub_soup = human_soup(base_url + subreddit)
# post_divs = get_post_divs(sub_soup)
# post_links = get_post_links(post_divs)
# # test_stuff(post_links)
# test_unusual_words(post_links)
