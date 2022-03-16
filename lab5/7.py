import re as regex
def tcm(b):
    return b.group(1) + b.group(2).capitalize()
def stc(a):
    print(regex.sub("(.*?)_([a-zA-Z])", tcm, a)) 

stc(input())