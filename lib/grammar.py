
def grammatical(string):
    if string[0].isupper():
        return True
    else: 
        return False
    

def punctuation(string):
    return string.endswith(".") or string.endswith("?") or string.endswith("!")