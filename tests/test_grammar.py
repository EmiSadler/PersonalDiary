import pytest
from lib.grammar import *

def test_capitals():
    assert grammatical("This is a sentence") == True
    assert grammatical("where is my capital?") == False

def test_punctuation():
    assert punctuation("Where is my question mark") == False
    assert punctuation("Did I find it?") == True