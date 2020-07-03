from soteris_anagram.anagram_game import AnagramGame

_test_dictionary = """cat
aligned
dealing
leading
arrest
rarest
raters
starer
"""


def test_anagram_game():
    game = AnagramGame(words=_test_dictionary)

    for _, (diff, words) in enumerate(
        {
            5: ["arrest", "rarest", "raters", "starer"],
            6: ["cat"],
            8: ["dealing", "leading"],
        }.items()
    ):

        puzzle = game.get_puzzle(diff)
        for word in words:
            assert puzzle.word != word
            assert puzzle.check_answer(word)


def test_tick_puzzles():
    game = AnagramGame(words=_test_dictionary)

    for _, (diff, words) in enumerate(
        {
            5: ["arrest", "rarest", "raters", "starer"],
            6: ["cat"],
            8: ["dealing", "leading"],
        }.items()
    ):

        puzzle = game.get_trick_puzzle(diff)
        for word in words:
            assert puzzle.word != word
            assert len(puzzle.word) == len(word) + 1
            assert not puzzle.check_answer(word)
            assert puzzle.is_trick()
