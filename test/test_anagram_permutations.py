import random

from soteris_anagram.bucketed_words import BucketedWords
from soteris_anagram.permutations import (
    PermutationOption,
    anagram_permutations,
    trick_anagram_permutations,
    valid_word_permutations,
)
from soteris_anagram.word_map import WordMap

_test_dictionary = """cat
dog
god
aligned
dealing
leading
arrest
rarest
raters
starer
"""


def test_wordmap_answers():
    map = WordMap(words=_test_dictionary)
    assert valid_word_permutations(map, "tac") == [
        PermutationOption(word="tca", minimum_distance=3),
        PermutationOption(word="atc", minimum_distance=3),
        PermutationOption(word="tac", minimum_distance=2),
        PermutationOption(word="act", minimum_distance=2),
        PermutationOption(word="cta", minimum_distance=2),
    ]
    assert valid_word_permutations(map, "notword") == []


def test_anagram_permutations():
    map = WordMap(words=_test_dictionary)
    buckets = BucketedWords(map)
    word = anagram_permutations(buckets, 6, map)
    assert word != "cat"
    assert set(word) == set("cat")


def test_trick_anagram_permutations():
    random.seed(1)
    map = WordMap(words=_test_dictionary)
    buckets = BucketedWords(map)
    word = trick_anagram_permutations(buckets, 6, map)
    assert set(word) == set("tcas")
