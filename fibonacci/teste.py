__author__ = 'rafael'

s = [0,1]
for i in range(100):
    v = s[0] + s[1]
    s[0], s[1] = s[1], v
    print(v)
