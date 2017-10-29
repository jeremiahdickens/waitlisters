"""
Main File:
Gets string from comments off reddit
passes string to emojiDictionary
Gets it back(converted)
passes to reply_post - posts to reddit
"""
import praw
import emojiDictionary
import emoji
import reply_post

subreddit = input("What subreddit's comments do you want to convert(Submit URL) - type d for default subreddit: ")
if (subreddit == "d"):
    subreddit = ("https://www.reddit.com/r/text2emoji/comments/79e46t/test_post/")

print("running...")

reddit = praw.Reddit('bot1') #Creating reddit instance

#Obtains submission object
submission = reddit.submission(url=subreddit)
submission.comments.replace_more(limit=0)

for top_level_comment in submission.comments:
    emojiString = emojiDictionary.toEmojiString((top_level_comment.body))
    emojiString = emoji.emojize(emojiString, use_aliases=True)
    if(emojiDictionary.lastHadEmoji() == True):
        print("To be posted to Reddit")
        print(emojiString)
        print()
        reply_post.replyMaster(emojiString, top_level_comment)
