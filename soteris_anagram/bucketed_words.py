import math
import random
from typing import List, Optional

import scipy.stats as stats

from soteris_anagram.word_map import WordMap


class BucketedWords(object):
    def __init__(self, word_map: WordMap):
        """
            Initializes the difficulty buckets using a function and a wordmap.
            Args:

            bucketfunc: Callable(int, int) -> int
                A function that takes an integer for the length of the string
                 and an integer for the number of answers and returns an integer 0-9
            word_map: WordMap
                A word map object to allocate difficulties to
        """
        self._build_histograms(word_map)
        self.buckets: List[List[str]] = [[] for _ in range(0, 10)]
        for _, (knapsack, answers) in enumerate(word_map.word_map.items()):
            if len(answers) == 0:  # these words have no anagrams
                continue
            s = word_map.letters_from_key(knapsack)
            diff = self.difficulty(len(s), len(answers))
            # print(len(s), len(answers), difficulty)
            self.buckets[diff].append(s)

    def get_word_with_difficulty(self, difficulty: int) -> Optional[str]:
        if len(self.buckets[difficulty]) == 0:
            print(self.buckets, difficulty, self.buckets[difficulty])
            return None
        return random.sample(self.buckets[difficulty], 1)[0]

    def _build_histograms(self, word_map):
        self.wordLengths = []
        self.n_answers = []
        for _, (knapsack, answers) in enumerate(word_map.word_map.items()):
            if len(answers) == 0:  # these words have no anagrams
                continue
            self.wordLengths.append(len(word_map.letters_from_key(knapsack)))
            self.n_answers.append(1.0 / len(answers))
        # TODO: histograms of actual percentile values could be precalculated and persisted to save time & memory
        self.wordLengths = random.sample(
            self.wordLengths, min(len(self.wordLengths), 512)
        )

        self.n_answers = random.sample(self.n_answers, min(len(self.n_answers), 512))

    def difficulty(self, lenWord: int, n_answers: int) -> int:
        word_length_weight = 6
        n_answers_weight = 4
        length_percentile = stats.percentileofscore(self.wordLengths, lenWord) / 100
        answers_percentile = (
            stats.percentileofscore(self.n_answers, 1.0 / n_answers) / 100
        )
        return math.floor(
            (
                word_length_weight * length_percentile
                + n_answers_weight * answers_percentile
            )
            / (word_length_weight + n_answers_weight)
            * 10
        )
