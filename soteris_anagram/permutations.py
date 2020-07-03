import random
from dataclasses import dataclass
from itertools import permutations
from typing import List, Optional

import textdistance

from soteris_anagram.bucketed_words import BucketedWords
from soteris_anagram.word_map import WordMap


@dataclass
class PermutationOption:
    word: str
    minimum_distance: int


def valid_word_permutations(
    word_map: WordMap, word: Optional[str]
) -> List[PermutationOption]:
    if word is None:
        return []
    options = []
    answers = word_map.correct_answers(word)
    if len(answers) == 0:
        return []
    for s in permutations(word):
        candidate = "".join(s)
        if not word_map.is_word(candidate):
            options.append(
                PermutationOption(
                    word=candidate,
                    minimum_distance=min(
                        map(lambda word: textdistance.hamming(candidate, word), answers)
                    ),
                )
            )
        if len(options) > 1000:
            break
    options.sort(key=lambda opt: -opt.minimum_distance)
    return options


def anagram_permutations(
    bucket_words: BucketedWords, difficulty: int, word_map: WordMap
) -> Optional[str]:
    """
        This returns non-dictionary-word permutations of the given word in
        descending order of distance from all the valid words
    """
    word = bucket_words.get_word_with_difficulty(difficulty)
    options = valid_word_permutations(word_map, word)
    return options[0].word


_common_letters = ["e", "t", "a", "o", "i", "n", "s"]


def trick_anagram_permutations(
    bucket_words: BucketedWords, difficulty: int, word_map: WordMap
) -> Optional[str]:
    for _ in range(0, 10):
        word = anagram_permutations(bucket_words, difficulty, word_map)
        if word is None:
            return None
        letters = _common_letters.copy()
        random.shuffle(letters)
        while len(letters) > 0:
            candidate = word + letters.pop()
            if word_map.is_knapsack_word(candidate):
                continue
            return candidate
    # This is unlikely, but possible. Could refactor to walk through difficulties?
    return None
