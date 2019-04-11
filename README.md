# twi2vec
using tweepy to crawl specific user's twitter, then use word2vec to vectorize the user.

## USAGE
First fill in the blank in `utils/account.py`, which contains Twitter API token information from your Twitter Dev Account.
``` python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'
```
After that, feel free to use any of the functions from `utils` ;)

## MILESTONES
- [x] Stream Twitter by keywords
- [ ] Extract specified user's twitter
- [ ] Implement Word2Vec
- [ ] Vectorize user's twitter
- [ ] Characterize user based on the extracted vector
- [ ] Compare user similarity based on vectors