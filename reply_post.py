#!/usr/bin/python
import praw
import pdb
import re
import os
import emoji

#print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
# recieving modified string, and the submission
def replyMaster(emojified_comment, submission):
    # Create the Reddit instance
    reddit = praw.Reddit('bot1')

    # Have we run this code before? If not, create an empty list
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []

    # If we have run the code before, load the list of posts we have replied to
    else:
        # Read the file into a list and remove any empty values
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    # If we haven't replied to this post before
    if submission not in posts_replied_to:
        # Reply to the comment
        submission.reply("Text2emoji bot: " + emojified_comment)

    # Write our updated list back to the file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
