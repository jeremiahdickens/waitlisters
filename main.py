#Main file
import praw


reddit = praw.Reddit('bot1') #Creating reddit instance

subreddit = reddit.subreddit("Learnpython")
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------\n")
