import re as regex
def match(a):
    p = '^[a-z]+_[a-z]+$'
    if regex.search(p, a):
        return 'Match'
    else:
        return 'Unmatch'

l = input()

print(match(l))