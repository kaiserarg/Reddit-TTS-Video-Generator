import sys
import praw
from praw.models import MoreComments
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
PASSWORD = os.getenv('PASSWORD')
USER_AGENT = os.getenv('USER_AGENT')
OATHUSER = os.getenv('OATHUSER')

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    password= PASSWORD,
    user_agent = USER_AGENT,
    username = OATHUSER,
)

if reddit.read_only:
    print('Failed to login, check your credentials')
    sys.exit()
else:
    print('Logged in successfully')

subreddit = reddit.subreddit("askreddit")

wordcount = 0 
comments = []

for submission in subreddit.top(limit=1, time_filter='week'):
    postTitle = submission.title
    print(submission.title)
    
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        wordcount += len(top_level_comment.body.strip().split(" "))

        if(wordcount < 200):
            comments.append(top_level_comment.body) 
        else: 
            break


        # limit it to 200 words,round down for comments 
print(comments)
print(len(comments))

