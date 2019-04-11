# twee2vec
using tweepy to crawl specific user's twitter, then use word2vec to vectorize the user.

## USAGE
### Account
First fill in the blank in `utils/account.py`, which contains Twitter API token information from your *Twitter Dev Account*.
``` python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'
```
After that, feel free to use any of the functions from `utils` :wink:

### Word2Vec
In order to use word2vec function, you need to first download pre-trained models from here:
> 'crawl-300d-2M-subword' by Facebook
> https://fasttext.cc/docs/en/english-vectors.html 

> 'GoogleNews-vectors-negative300' by Google
> https://code.google.com/archive/p/word2vec/

then place the models in `./model`, you are good to go.

## MILESTONES
- [x] Stream Twitter by keywords
- [x] Extract specified user's twitter
- [x] Implement Word2Vec
- [x] Vectorize user's twitter
- [ ] Characterize user based on the extracted vector
- [ ] Compare user similarity based on vectors
