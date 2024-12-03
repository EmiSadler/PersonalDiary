string = "This is a string that is longer than 5 words..."

def make_snippet(string):
    listed_string = string.split()
    if len(listed_string) > 5:
        snipped = listed_string[:5]
        snip = " ".join(snipped) + "..."
    return snip
    


