from get_data import NepaliCorpus
import re
import time


def test_data():
	start_time = time.time()
	nepali_hmm = NepaliCorpus()
	end_time = time.time()

	print('(Time to initialize Nepali Corpus: %s)' % (end_time - start_time))

	start_test_time = time.time()
	nepali_hmm.testHMM("./tagset/cs")
	end_test_time = time.time()

	print('(Time to test : %s)' % (end_test_time - start_test_time))

if __name__ == '__main__':
	test_data()