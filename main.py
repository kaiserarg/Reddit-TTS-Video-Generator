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

print(reddit.read_only)
# Output: False