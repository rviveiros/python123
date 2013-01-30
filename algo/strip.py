import string

def replace(s, chars):
    print(s, type(s))
    return s.replace(chars, "")

print(replace("hello world", "o"))