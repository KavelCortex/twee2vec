import gensim

def load_crawl():
    '''
    returns fasttext model 'crawl-300d-2M-subword' trained by Facebook https://fasttext.cc/docs/en/english-vectors.html 
    Approx time: 4 mins
    '''
    model_crawl = gensim.models.fasttext.load_facebook_model('models/crawl-300d-2M-subword.bin')
    return model_crawl

def load_googlenews():
    '''
    returns word2vec model 'GoogleNews-vectors-negative300' trained by Google https://code.google.com/archive/p/word2vec/
    Approx time: 3 mins
    '''
    model_googlenews = gensim.models.KeyedVectors.load_word2vec_format('models/GoogleNews-vectors-negative300.bin',binary=True)
    model_googlenews.simi
    return model_googlenews

