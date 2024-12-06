# File: lib/high_value.py

class HighValue:
    def __init__(self, value_first, value_second):
        self.value_first = value_first
        self.value_second = value_second
    def get_highest(self):
        if type(self.value_first) is int and type(self.value_second) is int:
            if self.value_first > self.value_second:
                return "First value is higher"
            elif self.value_first < self.value_second:
                return "Second value is higher"
            elif self.value_first == self.value_second:
                return "Values are equal"
        else:
            raise Exception("Values must be integers")
    def add(self, increase_by, selection):
        if selection == "first":
            self.value_first += increase_by
            return self.value_first
        elif selection == "second":
            self.value_second += increase_by
            return self.value_second
