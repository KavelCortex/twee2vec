import tweepy
from utils.account import auth,api
from utils.formatter import json_to_string
import json


class myStreamListener(tweepy.StreamListener):
    def __init__(self, save_dir=None):
        self.save_dir = save_dir

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        obj = json.loads(data)
        if self.save_dir:
            with open(self.save_dir, 'a') as f:
                f.write(data)
        else:
            print(json_to_string(obj))


def stream(keyword,save_dir=None):
    if type(keyword) is not list:
        keyword=[keyword]
    twitter_stream = tweepy.Stream(auth, myStreamListener(save_dir=save_dir))
    twitter_stream.filter(track=keyword)

def get_user_timeline(screen_name,limit=0):
    tweet_list=[]
    cursor = tweepy.Cursor(api.user_timeline,id=screen_name)
    
    for items in cursor.items(limit=limit):
        tweet_list.append(items)
    return tweet_list