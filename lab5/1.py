import re as regex
def match(a):
    p = 'a+?'
    if regex.search(p, a):
        return 'Match'
    else:
        return 'Unmatch'

l = input()

print(match(l))