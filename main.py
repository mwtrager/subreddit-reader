import praw
import webscraper as ws
import processing as pr

# TODO error checking
subreddit = input('enter a subreddit: ')

# get reddit
reddit = praw.Reddit(client_id='',
client_secret='',
user_agent='')

# get all links on the frontpage of this subreddit for PRAW to make object from these submissions
soup = ws.human_soup('https://www.reddit.com/r/'+subreddit+'/')
posts = ws.subreddit_frontpage(soup)
print('Number of posts being sent in:', len(posts))

# show all links generated
[print(post) for post in posts]

# count the # of comments reported by the web to compare to # of comments that the api returns
num_web_comments = ws.get_num_web_comments(soup)

num_api_comments = 0
num_posts = 0
unusuals_list = []
for post in posts:
    num_posts = num_posts + 1
    post = reddit.submission(url=post)
    print(post.title)
    post.comments.replace_more(limit=None)
    # TODO build these lists on the subreddit level
    raw_list = []
    tokens_list = []
    words_list = []
    vocab_list = []
    lemmas_list = []
    for comment in post.comments.list():
        num_api_comments = num_api_comments + 1
        raw = comment.body
        tokens = pr.tokenize(raw)
        words = pr.get_words(tokens)
        vocab = pr.get_vocab(words)
        lemmas = pr.lemmatize(sorted(vocab)) # NOTE sorted turns this to a list
        unusuals = pr.unusual_words(lemmas)

        raw_list.append(raw)
        tokens_list.append(tokens)
        words_list.append(words)
        vocab_list.append(vocab)
        lemmas_list.append(lemmas)
        if len(unusuals) > 0:
            unusuals_list.append(unusuals)

# flatten list
unusuals_list = [item for sublist in unusuals_list for item in sublist]
print(sorted(set(unusuals_list)))
print('number of posts being sent in:', len(posts))
print('number of posts processed:', num_posts)
print('number of api comments', num_api_comments)
print('number of web comments', num_web_comments)
