#Main file
"""
Gets string from comments off reddit
passes string to emojiDictionary
Gets it back(converted)
passes to poster
"""
import praw
import emojiDictionary
import emoji
import reply_post.py

print("running...")
reddit = praw.Reddit('bot1') #Creating reddit instance

#Obtains submission object (multiple ways to do this)
submission = reddit.submission(url='https://www.reddit.com/r/text2emoji/comments/79e46t/test_post/')
submission.comments.replace_more(limit=0)

for top_level_comment in submission.comments:
    emojiString = emojiDictionary.toEmojiString((top_level_comment.body))
    emojiString = emoji.emojize(emojiString, use_aliases=True)
    if(emojiDictionary.lastHadEmoji() == True):
        print(emojiString)
        print(top_level_comment)
        #Eventually pass to poster code
        reply(emojiString, top_level_comment)

def redditComments()



#To do:
#Change subreddit
#Change comment selection
