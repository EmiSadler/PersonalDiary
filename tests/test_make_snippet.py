import pytest
from lib.make_snippet import *

def test_make_snippet():
    snips = make_snippet("This is a string that is longer than 5 words...")
    assert snips == "This is a string that..."
    