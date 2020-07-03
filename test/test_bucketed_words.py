from soteris_anagram.bucketed_words import BucketedWords
from soteris_anagram.word_map import WordMap

_test_dictionary = """cat
aligned
dealing
leading
arrest
rarest
raters
starer
"""


# This is technically a flaky test, but unlikely to flail
def test_wordmap_answers():
    map = WordMap()
    buckets = BucketedWords(map)
    print([len(i) for i in buckets.buckets])
    for i in range(0, 8):
        assert len(buckets.buckets[i]) > 100


def test_simple_wordmap_answers():
    map = WordMap(words=_test_dictionary)
    buckets = BucketedWords(map)
    assert [len(i) for i in buckets.buckets] == [0, 0, 0, 0, 0, 1, 1, 0, 1, 0]
