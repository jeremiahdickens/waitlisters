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
#import time

loop = 0
while (loop < 1): #Eventually near infinite

    reddit = praw.Reddit('bot1') #Creating reddit instance

    userInput = input("What subreddit's comments do you want to convert(Submit name of subreddit) - type d for default subreddit: ")
    if (userInput == "d"):
        subreddit = reddit.subreddit('text2emoji')
        #subreddit = ("https://www.reddit.com/r/text2emoji/")
    else:
        subreddit = reddit.subreddit(userInput)

    print("running...")

    #Obtains submission object
    for submission in subreddit.hot(limit=10):
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments:
            emojiString = emojiDictionary.toEmojiString((top_level_comment.body))
            if not emojiString == False:
                emojiString = emoji.emojize(emojiString, use_aliases=True)
                if(emojiDictionary.lastHadEmoji() == True):
                    print("To be posted to Reddit")
                    print(emojiString)
                    print()
                    #reply_post.replyMaster(emojiString, top_level_comment)
    loop = loop + 1 #get rid of this once the while loop is infinite
    #time.sleep(30) #half a min.
