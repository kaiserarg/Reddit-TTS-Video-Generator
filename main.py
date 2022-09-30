import sys
import praw
from praw.models import MoreComments
import os
from dotenv import load_dotenv
from requests import post
from Upload.Youtube.upload_video import upload_Video




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
authors = []

for submission in subreddit.top(limit=1, time_filter='day'):
    postTitle = submission.title
    
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        wordcount += len(top_level_comment.body.strip().split(" "))
        title_len = len(postTitle.strip().split(" "))

        # limit it to 200 words,round down for comments 
        if(wordcount < 200 + title_len):
            comments.append(top_level_comment.body) 
            authors.append("u/" + top_level_comment.author.name + ": \n")
        else: 
            break

#insert postTitle to comments too so that the audio file plays the post title first
authors.insert(0, "u/" + submission.author.name + ": \n")
comments.insert(0, postTitle)



#uploads the video and automatically assigns it a title 
video_args = {
    "file": "test.mp4",
    "title": "Today in r/AskReddit: " + postTitle,
    "description": "placeholder ",
    "category": "22",
    "keywords": "reddit, askreddit, idk ", 
    "privacyStatus": "public"
}

upload_Video(video_args)





