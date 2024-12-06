from lib.diary import Diary
from lib.diary import DiaryEntry
import pytest

def test_counting_contents_string():
    title = "Monday 8am"
    content = "Woke up and made coffee"
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.count_words()
    assert result == 5

def test_counting_contents_empty():
    title = "Monday 9am"
    content = ""
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.count_words()
    assert result == 0

def test_counting_contents_other_data_types():
    title = "Monday 10am"
    content = 67
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.count_words()
    assert result == "Content type not supported"

def test_wpm_for_100_words():
    title = "Monday 11am"
    content = ("work " * 100)
    wpm = 10
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.reading_time(wpm)
    assert result == 10

def test_wpm_answer_is_float():
    title = "Monday 11am"
    content = ("work " * 1)
    wpm = 2
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.reading_time(wpm)
    assert result == 0.5

def test_wpm_for_zero_words():
    title = "Monday 12pm"
    content = ""
    wpm = 10
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.reading_time(wpm)
    assert result == 0

def test_wpm_is_zero():
    title = "Monday 1pm"
    content = "It was then she discovered, sadly, he could not read"
    wpm = 0
    diary_entry = DiaryEntry(title, content)
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "WPM must be greater than 0"

def test_short_reading_chunk():
    title = "Monday 2pm"
    content = "Is it time for an afternoon nap? Sure feels it!"
    wpm = 2
    minutes = 1
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "Is it"
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "time for"
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "an afternoon"