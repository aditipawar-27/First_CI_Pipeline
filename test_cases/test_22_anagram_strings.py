import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_basic_anagram():
    assert is_anagram("listen", "silent") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_case_is_ignored():
    assert is_anagram("Listen", "SILENT") is True


def test_spaces_are_ignored():
    assert is_anagram("Dormitory", "Dirty room") is True


def test_different_lengths():
    assert is_anagram("abc", "abcd") is False


def test_same_letters_different_counts():
    assert is_anagram("aab", "abb") is False


def test_empty_strings():
    assert is_anagram("", "") is True
