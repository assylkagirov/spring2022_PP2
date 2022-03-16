import re as regex
def match(a):
    p = '[A-Z]+[a-z]+$'
    if regex.search(p, a):
        return 'Match'
    else:
        return 'Unmatch'

l = input()

print(match(l))