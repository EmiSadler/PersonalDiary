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

def test_odd_numbers():
    title = "Monday 2:30pm"
    content = "Eyes are getting heavy, but I must push through it!"
    wpm = 3
    minutes = 1
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "Eyes are getting"
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "heavy, but I"
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "must push through"
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "it!"

def test_reading_more_text():
    title = "Monday 3pm"
    content = "Post nap and ready to return to my job as a code Monkey"
    wpm = 7
    minutes = 1
    diary_entry = DiaryEntry(title, content)
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "Post nap and ready to return to"
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "my job as a code Monkey"
    result = diary_entry.reading_chunk(wpm, minutes)
    assert result == "Post nap and ready to return to"

def test_adding_an_entry():
    # SETUP
    title = "Monday 4pm"
    content = "Snack aquired, ready to sort out this bug in my code!"
    entry = DiaryEntry(title, content)
    diary = Diary()

    #LOGIC
    diary.add(entry)

    # ASSERTION
    assert diary.list_of_entries == [entry]
    
def test_all_entries():
    title = "Monday 5pm"
    content = "Wrote my to-do list for tomorrow based on what I didn't finish today, and oooh boy, it is a doozy!"
    entry = DiaryEntry(title, content)
    title2 = "Monday 6pm"
    content2 = "Stepped outside from the office to find my bicycle has been stolen!"
    entry2 = DiaryEntry(title2, content2)
    diary = Diary()
    diary.add(entry)
    diary.add(entry2)
    assert diary.list_of_entries == [entry, entry2]

def test_count_all_words():
    title = "Monday 7pm"
    content = "Took the bus home"
    entry = DiaryEntry(title, content)
    title2 = "Monday 8pm"
    content2 = "Found my bike in the garden... forgot I drove my car to work..."
    entry2 = DiaryEntry(title2, content2)
    diary = Diary()
    diary.add(entry)
    diary.add(entry2)
    result = diary.count_words()
    assert result == 17

def test_reading_time_wpm_is_one():
    title = "Monday 9pm"
    content = "Cooked a very late dinner, lasagna, because like Garfield, I hate Mondays."
    wpm = 1
    entry = DiaryEntry(title, content)
    diary = Diary()
    diary.add(entry)
    result = diary.reading_time(wpm)
    assert result == 12

def test_reading_time_two_entries_twelve_words_one_minute():
    wpm = 12
    title = "Monday 10pm"
    content = "Cleaned up from dinner, had a shower"
    entry = DiaryEntry(title, content)
    title2 = "Monday 11pm"
    content2 = "Time to tuck into bed"
    entry2 = DiaryEntry(title2, content2)
    diary = Diary()
    diary.add(entry)
    diary.add(entry2)
    result = diary.reading_time(wpm)
    assert result == 1

def test_reading_time_two_entries_both_are_empty():
    wpm = 10
    title = "Tuesday 12am"
    content = ""
    entry = DiaryEntry(title, content)
    title2 = "Tuesday 1am"
    content2 = ""
    entry2 = DiaryEntry(title2, content2)
    diary = Diary()
    diary.add(entry)
    diary.add(entry2)
    result = diary.reading_time(wpm)
    assert result == 0

def test_reading_time_two_entries_one_is_empty():
    wpm = 3
    title = "Tuesday 2am"
    content = ""
    entry = DiaryEntry(title, content)
    title2 = "Tuesday 3am"
    content2 = "Woke with a jolt! I haven't paid for overnight parking for my car in the garage... tomorrow is going to be a long day."
    entry2 = DiaryEntry(title2, content2)
    diary = Diary()
    diary.add(entry)
    diary.add(entry2)
    result = diary.reading_time(wpm)
    assert result == 8

def test_find_best_entry_title_one_exact():
    wpm = 3
    minutes = 1
    title = "Tuesday 4am"
    content = "zzz, zzz, zzz"
    title2 = 'Tuesday 5am'
    content2 = "I woke up to my alarm this morning, crawled out of bed and made myself some coffee."
    entry = DiaryEntry(title, content)
    entry2 = DiaryEntry(title2, content2)
    diary = Diary()
    diary.add(entry)
    diary.add(entry2)
    result = diary.find_best_entry_for_reading_time(wpm, minutes)
    assert result == entry

def test_find_best_entry_mid_way_ish():
    wpm = 6
    minutes = 3
    title = "Tuesday 6am"
    content = "Reremembered that my car is at work, so I'll catch the bus into the office."
    title2 = "Tuesday 7am"
    content2 = "Sat on bus and read the newspaper"
    title3 = "Tuesday 8am"
    content3 = "Arrived at the office and went to check on car, no ticket! Woo! Paid for another day of parking. Headed inside the office to see that my friend had sent a fruit basket. Today is a great day!"
    entry = DiaryEntry(title, content)
    entry2 = DiaryEntry(title2, content2)
    entry3 = DiaryEntry(title3, content3)
    diary = Diary()
    diary.add(entry)
    diary.add(entry2)
    diary.add(entry3)
    result = diary.find_best_entry_for_reading_time(wpm, minutes)
    assert result == entry3

# def test_two_entries_the_same_length():
#     wpm = 2
#     minutes = 2
#     title = "Tuesday 9am"
#     content = "Code Monkey write code"
#     title2 = "Tuesday 10am"
#     content2 = "Code Monkey make coffee"
#     entry = DiaryEntry(title, content)
#     entry2 = DiaryEntry(title2, content2)
#     diary = Diary()
#     diary.add(entry)
#     diary.add(entry2)
#     result = diary.find_best_entry_for_reading_time(wpm, minutes)
#     assert result == f"You could choose this entry: {entry} or this entry: {entry2}."