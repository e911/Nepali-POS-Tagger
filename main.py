from get_data import NepaliCorpus
import re
import time


def get_user_input():
    return re.sub(r"([\.,?])", r" \1 ", input("\033[95mEnter your sentence ('stop' to exit): \033[0m"))


def start_tagger():
    start_time = time.time()
    nepali_hmm = NepaliCorpus()
    end_time = time.time()

    print('(Time to initialize Nepali Corpus: %s)' % (end_time - start_time))

    user_input = get_user_input()
    while user_input != 'stop':
        start_time = time.time()
        sentence = user_input.split()
        y = nepali_hmm.get_tag_sequence(sentence)
        end_time = time.time()
        
        if y == '':
            print("Please input text and retry")
        else:
            print("\nThe best tag sequence is:", y)
            print('(Time to tag this sentence: %s)' % (end_time - start_time))

        user_input = get_user_input()

if __name__ == '__main__':
    print('Initializing the tagger...')
    print("Please wait...")
    start_tagger()
