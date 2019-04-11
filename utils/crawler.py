from tweepy import Stream, StreamListener
from utils.account import auth
from utils.format import json_to_string
import json


class CrawlListener(StreamListener):
    def __init__(self, save_dir=None):
        self.save_dir = save_dir

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        obj = json.loads(data)
        if self.save_dir:
            with open(save_dir, 'a') as f:
                f.write(data)
        else:
            print(json_to_string(obj))


def crawl(keyword,save_dir=None):
    if type(keyword) is not list:
        keyword=[keyword]
    twitter_stream = Stream(auth, CrawlListener(save_dir=save_dir))
    twitter_stream.filter(track=keyword)
