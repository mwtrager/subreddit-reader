import nltk # yep

# we're only working with text here. nothing else.
# no soup, nothing. this is a clean page.

# what do we want here?

# give me the OP as a single list of characters
# give me the a list comments, each being a list of words
# this module will process those incoming lists of text

# combine the op and comment text lists

# tokenize the op

# tokenize the comments

# tokenize both combined

# calculate lexical diversity

def combine_op_comments(op, comments):
    return text

def tokenize(text):
    # check to see if this is a list or not
    # if its not a list tokenize it
    # if it is a list loop through and tokenize
    # IDEA i wonder if nltk does this with nltk.word_tokenize()



# find all divs with class usertext-body
divs = soup('div', class_='usertext-body')

# HACK ignore the first one because its the sidebar
divs = divs[1:]

# tokenize comments
posts_tokenized = []
for div in divs:
    # use div.get_text to get all text of all children nodes to div.usertext-body
    # BUG we ignore emphasis by ignoring bold words, italics, and other html inline formatting
    text = div.get_text()
    tokens = nltk.word_tokenize(text)
    # print(tokens)
    posts_tokenized.append(tokens)

return posts_tokenized
