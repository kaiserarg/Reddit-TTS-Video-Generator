import sys
import praw
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID'),
CLIENT_SECRET = os.getenv('CLIENT_SECRET'),
PASSWORD = os.getenv('PASSWORD'),
USER_AGENT = os.getenv('USER_AGENT'),
USERNAME = os.getenv('USERNAME'),


reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    password= PASSWORD,
    user_agent = USER_AGENT,
    username = USERNAME,
)

if reddit.read_only:
    print('Failed to login, check your credentials')
    sys.exit()
else:
    print('Logged in successfully')

