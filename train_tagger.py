from get_data import NepaliCorpus
from nltk.tag import tnt

def train(tnt_tagger):
    nepali_hmm = NepaliCorpus()
    tags = nepali_hmm.get_tags()
    train_data = tags[:3000]
    test_data = tags[3000:3500]
    tnt_tagger.train(train_data)

