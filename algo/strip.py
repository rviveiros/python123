
def stripChars(s, chars):
    return s.translate(None, chars)

print stripChars("hello world", "o")