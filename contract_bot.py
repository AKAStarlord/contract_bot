#  Author:      Tim Dale
#               timdale7@gmail.com
#
#  This bot is intended to use the General Fanager public API to serve user requests on www.reddit.com/r/hockey
#  using PRAW to communicate to the Reddit API.

import praw
import time
from pprint import pprint


# Check to see if this is a comment we want to perform an action on and returns the appropriate index.
def check_conditions(com):
    text = com.body
    tokens = text.split()
    for tok in tokens:
        for word in keyWords:
            if word == tok:
                return tokens.index(tok)
    return None


# Perform the relevant General Fanager API work.
def bot_action(com, ind):
    text = com.body
    tokens = text.split()
    player_name = tokens[ind + 1] + " " + tokens[ind + 2]  # Combine the first and last name of a player.
    print(player_name)  # Debug.
    result = call_general_fanager_api(player_name=player_name)
    readable_message = build_response(api_result=result)
    send_response(readable_message)
    return


# Sends the API request to General Fanager and returns the result.
def call_general_fanager_api(player_name):
    # TODO implement this once we get access to General Fanager's public API.
    api_result = ""
    return api_result


# Builds a human/reddit readable comment to be submitted back to the user.
def build_response(api_result):
    # TODO implement once we know how General Fanager handles it's data.
    return


# Sends and posts the finished message back to the user.
def send_response(complete_message):
    # TODO once build_response is complete.
    return

VER_NUM = 0.1

user_agent = "Contract_Info v" + repr(VER_NUM) + " by /u/HORSEtheGAME"
r = praw.Reddit(user_agent=user_agent)

user_name = "contract-bot"
user = r.get_redditor(user_name)

r.login()  # TODO This function is depreciated.

thing_limit = 10  # TODO This is a temporary measure during development.

# For now we are only interested in /r/hockey. In future versions I'd like to expand to NHL team subreddits.
subreddit = r.get_subreddit('hockey')

keyWords = ['!contract-bot', '!contract_bot']  # These are the keywords we'll look for when searching comments.

# This should read in all new comments indefinitely from /r/hockey.
for comment in praw.helpers.comment_stream(reddit_session=r, subreddit=subreddit):
    key_token = check_conditions(com=comment)

    if key_token is not None:
        bot_action(com=comment, ind=key_token)

# TODO Solve the three bot problems:

# Not doing the same work twice:
# We'll know we haven't read in the same comment twice if the comment we're reading has a child comment submitted
# by our bot.

# Running continually:
# We probably don't care if Reddit crashes. We won't be holding onto any important information. If Reddit crashes then
# it is probably OK that our bot crashes as well. However we'll have to figure out how to handle a restart.

# Keeping within API guidelines:
# PRAW should handle this for us. Be sure to read the API guidelines, etc.
