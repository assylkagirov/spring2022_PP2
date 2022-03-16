import re as regex
def turnintosnake(a):
    a = '_'.join(regex.sub('([A-Z][a-z]+)', r' \1', regex.sub('([A-Z]+)', r' \1', a.replace('-', ' '))).split()).lower()
    print(a)

turnintosnake(input())