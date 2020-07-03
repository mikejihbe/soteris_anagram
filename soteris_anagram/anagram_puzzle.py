from typing import List, Optional


class AnagramPuzzle(object):
    def __init__(self, word: Optional[str], answers: Optional[List[str]]):
        self.word = word
        self.answers = answers

    def check_answer(self, guess: str):
        return self.answers is not None and guess in self.answers

    def is_trick(self):
        return False


class AnagramTrickPuzzle(AnagramPuzzle):
    def __init__(self, word: Optional[str]):
        super().__init__(word=word, answers=None)

    def check_answer(self, guess: str):
        return False

    def is_trick(self):
        return True
