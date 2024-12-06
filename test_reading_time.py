from lib.reading_time import *

def test_reading_time():
    assert reading_time(400) == 2
    assert reading_time(800) == 4