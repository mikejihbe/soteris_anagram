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
    assert map.correct_answers("cat") == ["cat"]
    assert map.correct_answers("aligned") == ["aligned", "dealing", "leading"]
    assert map.correct_answers("arrest") == ["arrest", "rarest", "raters", "starer"]
    assert map.correct_answers("srrtae") == ["arrest", "rarest", "raters", "starer"]


def test_wordmap_words():
    map = WordMap(words=_test_dictionary)
    assert map.is_word("cat")
    assert not map.is_word("cta")
