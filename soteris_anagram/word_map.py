from typing import Dict, FrozenSet, List, Tuple


class WordMap(object):
    def __init__(self, wordfile: str = "/usr/share/dict/words", words: str = None):
        """
            Initializes the wordmap. We do no string modification, so clean your dictionary!
            Args:

            wordfile (optional, default): str
                The path to a dictionary. We assume no duplicates.
            words: str
                A string with newlines separating each word.
        """
        self.word_map: Dict[FrozenSet[Tuple[str, int]], List[str]] = {}
        if words is not None:
            self._init_word_map_from_string(words)
        else:
            with open(wordfile, "r") as file:
                words = file.read()
                self._init_word_map_from_string(words)

    def correct_answers(self, word: str) -> List[str]:
        return self.word_map.get(self._word_knapsack(word), [])

    def is_word(self, word: str) -> bool:
        return word in self.word_map.get(self._word_knapsack(word), [])

    def is_knapsack_word(self, letters: str) -> bool:
        return self._word_knapsack(letters) in self.word_map

    def letters_from_key(self, knapsack: FrozenSet[Tuple[str, int]]) -> str:
        return "".join(map(lambda t: t[1] * t[0], list(knapsack)))

    def _init_word_map_from_string(self, words: str) -> None:
        """
            Initializes the wordmap

            Args:
                words: str
                A string with newlines separating each word. We do no string modification, so clean your dictionary!
        """
        word_list = filter(
            lambda s: s != "", map(lambda s: s.strip(), words.split("\n"))
        )
        for _, word in enumerate(word_list):
            knapsack = self._word_knapsack(word)
            if knapsack in self.word_map:
                self.word_map[knapsack].append(word)
            else:
                self.word_map[knapsack] = [word]

    def _word_knapsack(self, word: str) -> FrozenSet[Tuple[str, int]]:
        """
            Python won't hash dictionaries for you because they're mutable, so we return a frozenset
        """
        knapsack: Dict[str, int] = {}
        for _, c in enumerate(word):
            if c in knapsack:
                knapsack[c] += 1
            else:
                knapsack[c] = 1
        return frozenset(knapsack.items())
