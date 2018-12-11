"""Test the frequency puzzle"""

import pytest

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
    assert frequency.update_frequency(0, 1) == 1

def test_update_frequency_counts_down_with_negatives():
    assert frequency.update_frequency(0, -1) == -1

def test_update_frequency_unchanged_with_zeroes():
    assert frequency.update_frequency(0, 0) == 0
