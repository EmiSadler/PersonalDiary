# File: lib/diary.py

class Diary:
    def __init__(self):
        self.list_of_entries = []

    def add(self, entry):
        self.list_of_entries.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list

    def all(self):
        return self.list_of_entries
        # Returns:
        #   A list of instances of DiaryEntry

    def count_words(self):
        words = 0
        for entry in self.list_of_entries:
            words_per_entry = DiaryEntry.count_words(entry)
            words += words_per_entry
        return words

        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
    

    def reading_time(self, wpm):
        total_words = Diary.count_words(self)
        time_in_minutes = total_words / wpm
        return time_in_minutes
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        time_to_read = wpm * minutes
        best_entry = None
        closest_time = 0
        for entry in self.list_of_entries:
            entry_time = entry.reading_time(wpm)
            if entry_time <= time_to_read and entry_time > closest_time:
                closest_time = entry_time
                best_entry = entry
        return best_entry
            
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.read_so_far = 0
        self.total_time = 0
        # Side-effects:
        #   Sets the title and contents properties

    def __repr__(self):
        return f"Title: {self.title}, Contents: {self.contents}"
        

    def count_words(self):
        if isinstance(self.contents, str):
            listed_content = self.contents.split()
            return len(listed_content)
        else:
            return "Content type not supported"

        # Returns:
        #   An integer representing the number of words in the contents
        

    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("WPM must be greater than 0")
        else:
            total_words = self.count_words() 
            self.total_time = total_words / wpm
            return self.total_time
        
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self.contents.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end = min(self.read_so_far + words_user_can_read, len(words))
        chunk_of_text = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_of_text)
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.