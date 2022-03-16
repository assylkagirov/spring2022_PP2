import re as regex
def match(a):
    p = 'ab{2,3}$'
    if regex.search(p, a):
        return 'Match'
    else:
        return 'Unmatch'

l = input()

print(match(l))