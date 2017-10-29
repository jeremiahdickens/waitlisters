#Main file
import praw
import emojiDictionary
import emoji

#Old code

print("running")
reddit = praw.Reddit('bot1') #Creating reddit instance

"""
subreddit = reddit.subreddit("Learnpython")
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------\n")
"""

#Obtains submission object (multiple ways to do this)
submission = reddit.submission(url='https://www.reddit.com/r/pythonforengineers/comments/79d7cw/hello_bot/')
submission.comments.replace_more(limit=0)

for top_level_comment in submission.comments:
    #print(top_level_comment.body)
    smile = emojiDictionary.toEmojiString((top_level_comment.body))
    smile = emoji.emojize(smile, use_aliases=True)
    if(emojiDictionary.lastHadEmoji() == True):
        print(smile)
