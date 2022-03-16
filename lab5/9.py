import re as regex
def cws(a):
    print(regex.sub(r"(\w)([A-Z])", r"\1 \2", a))

cws(input())