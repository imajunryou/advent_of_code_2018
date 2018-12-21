"""Test the frequency puzzle"""

import pytest

from oset import oset

import frequency


negatives = [("-1", -1), ("-10", -10), ("-1000", -1000)]
positives = [("+1", 1), ("+10", 10), ("+1000", 1000)]
nonnumerics = ["This is a list of letters", "表ポあA鷗ŒéＢ逍Üßªąñ丂㐀𠀀"]

@pytest.mark.parametrize('given, expected', negatives)
def test_parse_frequency_handles_negatives(given, expected):
    assert frequency.parse_frequency(given) == expected

@pytest.mark.parametrize('given, expected', positives)
def test_parse_frequency_handles_positives(given, expected):
    assert frequency.parse_frequency(given) == expected

@pytest.mark.parametrize('given', nonnumerics)
def test_parse_frequency_handles_nonnumerics(given):
    assert frequency.parse_frequency(given) == 0

def test_update_frequency_counts_up_with_positives():
    assert frequency.update_frequency(oset([0]), 1) == (oset([0, 1]), 1)

def test_update_frequency_counts_down_with_negatives():
    assert frequency.update_frequency(oset([0]), -1) == (oset([0, -1]), -1)

def test_update_frequency_unchanged_with_zeroes():
    assert frequency.update_frequency(oset([1]), 0) == (oset([1]), 1)

def test_has_repeat_returns_false_without_repeat():
    initial = oset([0, 1])
    initial_size = len(initial)
    final, subtotal = frequency.update_frequency(initial, 1)
    assert initial_size != len(final)

def test_has_repeat_returns_true_with_repeat():
    initial = oset([3, 2])
    final, subtotal = frequency.update_frequency(initial, 1)
    assert len(initial) == len(final)

sets = [
    (oset([3]), -1, (oset([3, 2]), 2)),
    (oset([3, 2]), 2, (oset([3, 2, 4]), 4)),
    (oset([3, 2]), 1, (oset([3, 2]), 3)),
    (oset([0, 3, 6, 10, 8]), -4, (oset([0, 3, 6, 10, 8, 4]), 4))
]
@pytest.mark.parametrize('past_frequencies, next_frequency, expected_frequencies', sets)
def test_frequency_subtotals_are_insertion_ordered(past_frequencies, next_frequency, expected_frequencies):
    assert frequency.update_frequency(past_frequencies, next_frequency) == expected_frequencies

repeatables = [
    (0, [3, 3, 4, -2, -4], 10),
    (0, [1, -1], 0),
    (0, [-6, 3, 8, 5, -6], 5),
    (0, [7, 7, -2, -7, -4], 14)
]
@pytest.mark.parametrize('initial, frequencies, expected', repeatables)
def test_repeating_updates_loops_until_results_found(initial, frequencies, expected):
    initial_set = oset([initial])
    assert frequency.find_repeat(initial_set, frequencies) == expected
    
