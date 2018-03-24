
# coding: utf-8

# In[28]:


# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json


# In[29]:


# Twitter API Keys
consumer_key = "r4b58sAz2lqEQZj3DpMkc0ibi"
consumer_secret = "kHH72T9XrpzGHJAgdVRZAlaRLEeDPm0AujM2pdNQpU4uhVxgUJ"
access_token = "975021712332017665-beqYO52oVSm94MsENtMoMY0XrJc9x1F"
access_token_secret = "5a2BWlPfRKxONfShepLlj2farPcNnkSdH9Kz9ODCR45mu"


# In[30]:


# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[31]:


# Target Term
my_username = "@BattleBot_1"
conversation_partner = "@BattleBot_2"


# In[32]:


# Send opening message to conversation partner
api.update_status("Hey %s! Whats going on?" % conversation_partner)


# In[ ]:



# Response Lines
# @TODO: Create a list of Response Lines
response_lines = [
    "@BattleBot_2 Nothing Much"
]


# In[ ]:


# # @TODO: Create converse function
def Converse(line_number):
    
#     # @TODO: Find the latest tweet from conversation_partner
    public_tweets = api.search(conversation_partner, count=1, result_type="recent")
    for tweet in public_tweets["statuses"]:
        print(tweet)


# In[ ]:


# @TODO: Respond to the tweet with one of the response lines
tweet_id = tweet["id"]
print(tweet_id)
print(tweet["text"])
api.update_status
response_line[line_number]
in_reply_to_status_id = tweet_id


# In[ ]:


# @TODO: Set timer to run every minute
counter = 0

while(True):
    time.sleep(60)
    Converse(counter)
    counter+1

