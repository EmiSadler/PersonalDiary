import pytest
from lib.altogether import *

def test_format():
    title = "My Title"
    contents = "These are the words in my contents"
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.format()
    assert result == "My Title: These are the words in my contents" 

def test_count_words():
    title = None
    contents = "This is a string of words that I will turn into a list to count."
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.count_words()
    assert result == 16

def test_reading_time_two_wpm():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1.5

def test_reading_chunk():
    title = "A Title Has Capital Letters"
    contents = "One, Two, Three, Four, Five, Six, Seven, Eight"
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_chunk(2, 1)
    assert result == "One, Two,"

def test_reading_double_the_chunks():
    title = "A Title Has Capital Letters"
    contents = "One, Two, Three, Four, Five, Six, Seven, Eight"
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_chunk(4, 2)
    assert result == "One, Two, Three, Four, Five, Six, Seven, Eight"

def test_check_fullstop():
    text = "This is a proper sentence."
    diary_entry = GrammarStats()
    result = diary_entry.check(text)
    assert result == True

def test_check_no_capital():
    text = "this is not a proper sentence?"
    diary_entry = GrammarStats()
    result = diary_entry.check(text)
    assert result == False

def test_check_exclamation():
    text = "Has a capital and ends with excitement!"
    diary_entry = GrammarStats()
    result = diary_entry.check(text)
    assert result == True

def test_check_nothing():
    text = ""
    diary_entry = GrammarStats()
    result = diary_entry.check(text)
    assert result == False

def test_multiple():
    stats = GrammarStats()
    assert stats.check("I am good at grammar.") == True
    assert stats.check("Can I use a question mark here?") == True
    assert stats.check("I could even use an exclamation mark!")
    assert stats.check("i've forgotten everything I thought I knew") == False
    assert stats.check("just an error at the start.") == False
    assert stats.check("At least I recognised that") == False
    result = stats.percentage_good()
    assert result == 50

def test_percent_100():
    stats = GrammarStats()
    assert stats.check("This is working all the time.") == True
    assert stats.check("Seriously, I am so good at grammar!") == True
    result = stats.percentage_good()
    assert result == 100

def test_percent_zero():
    stats = GrammarStats()
    assert stats.check("i am bad at stuff") == False
    assert stats.check("and things") == False
    assert stats.check("Oh so very bad") == False
    assert stats.check("so so so bad!") == False
    result = stats.percentage_good()
    assert result == 0