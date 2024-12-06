class DiaryEntry:
        # Parameters:
        #   title: string
        #   contents: string
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    # Returns:
    #   A formatted diary entry, for example:
    #   "My Title: These are the contents"
    def format(self):
        return f"{self.title}: {self.contents}"

    # Returns:
    # int: the number of words in the diary entry
    def count_words(self):
        listed_contents = self.contents.split()
        word_count = len(listed_contents) + 1
        return word_count

        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
    def reading_time(self, wpm):
        diary_entry = DiaryEntry(self.title,self.contents)
        result = diary_entry.count_words()
        time = result / wpm
        return time

        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
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
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
class GrammarStats:
    def __init__(self):
        self.passes = 0
        self.total = 0

    def check(self, text):
        self.total += 1
        if text == "":
            return False
        elif text[0].isupper() and (text.endswith(".") or text.endswith("?") or text.endswith("!")):
            self.passes += 1
            return True
        else:
            return False

        # Returns:
        #  int: the percentage of texts checked so far that passed the check
        # defined in the `check` method. The number 55 represents 55%.
    
    def percentage_good(self):
        return (self.passes / self.total) * 100
        



