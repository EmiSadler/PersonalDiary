import pytest
from lib.count_words import *

def test_count_words():
    word_count = count_words("This string has five words.")
    assert word_count == 5