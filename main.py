import utils.crawler as crawler
import utils.vectorizer as vectorizer
import model

# streaming
crawler.stream(['overwatch','baptiste'])

# timeline
tweet_list=crawler.get_user_timeline('alsareini',limit=0)
print(len(tweet_list))

# vectorize user
wv_model=model.load_crawl()
vector=vectorizer.vectorize_user(wv_model,'alsareini',limit=100)
print(vector)