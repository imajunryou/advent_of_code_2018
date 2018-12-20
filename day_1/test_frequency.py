"""Test the frequency puzzle"""

import pytest

from ordered_set import OrderedSet

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
    assert frequency.update_frequency(OrderedSet([0]), 1) == (OrderedSet([0, 1]), 1)

def test_update_frequency_counts_down_with_negatives():
    assert frequency.update_frequency(OrderedSet([0]), -1) == (OrderedSet([0, -1]), -1)

def test_update_frequency_unchanged_with_zeroes():
    assert frequency.update_frequency(OrderedSet([1]), 0) == (OrderedSet([1]), 1)

def test_has_repeat_returns_false_without_repeat():
    initial = OrderedSet([0, 1])
    final, subtotal = frequency.update_frequency(initial, 1)
    assert frequency.has_repeat(initial, final) == False

def test_has_repeat_returns_true_with_repeat():
    initial = OrderedSet([3, 2])
    final, subtotal = frequency.update_frequency(initial, 1)
    assert frequency.has_repeat(initial, final) == True

sets = [
    (OrderedSet([3]), -1, (OrderedSet([3, 2]), 2)),
    (OrderedSet([3, 2]), 2, (OrderedSet([3, 2, 4]), 4)),
    (OrderedSet([3, 2]), 1, (OrderedSet([3, 2]), 3)),
    (OrderedSet([0, 3, 6, 10, 8]), -4, (OrderedSet([0, 3, 6, 10, 8, 4]), 4))
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
    initial_set = OrderedSet([initial])
    assert frequency.find_repeat(initial_set, frequencies) == expected
    
