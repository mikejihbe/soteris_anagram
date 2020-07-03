from soteris_anagram.anagram_puzzle import AnagramPuzzle, AnagramTrickPuzzle
from soteris_anagram.bucketed_words import BucketedWords
from soteris_anagram.permutations import (
    anagram_permutations,
    trick_anagram_permutations,
)
from soteris_anagram.word_map import WordMap


class AnagramGame(object):
    def __init__(self, words=None, dict_file="/usr/share/dict/words"):
        self.word_map = WordMap(wordfile=dict_file, words=words)
        self.buckets = BucketedWords(self.word_map)

    def get_puzzle(self, difficulty: int):
        if difficulty < 0 or difficulty > 8:
            raise Exception("get_puzzle must be called with a difficulty between 1-8")

        puzzle = anagram_permutations(self.buckets, difficulty, self.word_map)
        return AnagramPuzzle(word=puzzle, answers=self.word_map.correct_answers(puzzle))

    def get_trick_puzzle(self, difficulty: int):
        if difficulty < 0 or difficulty > 8:
            raise Exception(
                "get_trick_puzzle must be called with a difficulty between 1-8"
            )

        puzzle = trick_anagram_permutations(self.buckets, difficulty, self.word_map)
        return AnagramTrickPuzzle(word=puzzle)
