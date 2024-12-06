from lib.EtienneEmily import *
import pytest

def test_get_first():
    value_first = 10
    value_second = 4
    highest = HighValue(value_first, value_second)
    result = highest.get_highest()
    assert result == "First value is higher"

def test_get_second():
    value_first = 4
    value_second = 10
    highest = HighValue(value_first, value_second)
    result = highest.get_highest()
    assert result == "Second value is higher"

def test_get_equal():
    value_first = 4
    value_second = 4
    highest = HighValue(value_first, value_second)
    result = highest.get_highest()
    assert result == "Values are equal"

def test_negatives():
    value_first = -4
    value_second = -14
    highest = HighValue(value_first, value_second)
    result = highest.get_highest()
    assert result == "First value is higher"

def test_empty():
    value_first = "one"
    value_second = 16
    highest = HighValue(value_first, value_second)
    with pytest.raises(Exception) as e:
        highest.get_highest()
    error_message = str(e.value)
    assert error_message == "Values must be integers"

def test_add_first():
    value_first = 5
    value_second = 10
    selection = "first"
    increase_by = 5
    add = HighValue(value_first, value_second)
    value_first = add.add(increase_by, selection)
    assert value_first == 10

def test_add_second():
    value_first = 5
    value_second = 10
    selection = "second"
    increase_by = 5
    add = HighValue(value_first, value_second)
    value_second = add.add(increase_by, selection)
    assert value_second == 15

def test_add_by_neg():
    value_first = 5
    value_second = 10
    selection = "second"
    increase_by = -1
    add = HighValue(value_first, value_second)
    value_second = add.add(increase_by, selection)
    assert value_second == 9

def test_both_changes():
    value_first = 5
    value_second = 10
    selection = "first"
    increase_by = 20
    add = HighValue(value_first, value_second)
    value_first = add.add(increase_by, selection)
    highest = HighValue(value_first, value_second)
    result = highest.get_highest()
    assert result == "First value is higher"
