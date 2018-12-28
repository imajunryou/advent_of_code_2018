import pytest
from checksum import has_counts, has_two, has_three, total_counts

def test_word_has_two_of_at_least_one_letter():
    given = "abbcde"
    assert has_two(given) == True

def test_word_has_three_of_at_least_one_letter():
    given = "abcccd"
    assert has_three(given) == True

def test_word_has_both_two_and_three_of_some_letters():
    given = "bababc"
    assert has_counts(given) == (True, True)

def test_word_has_no_pairs_or_triples():
    given = "abcde"
    assert has_counts(given) == (False, False)

def test_word_scores_accumulates_doubles():
    given = ["aab", "aba"]
    assert total_counts(given) == (2, 0)

def test_word_scores_accumulates_triples():
    given = ["abaca", "abcbdbq"]
    assert total_counts(given) == (0, 2)

def test_word_scores_accumulates_both():
    given = ["aab", "ababa", "aabab"]
    assert total_counts(given) == (3, 2)
