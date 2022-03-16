def todecimal(s):
    if not s:
        return 0
    return todecimal(s[:-1]) * 2 + int(s[-1])

x = str(input())

print(todecimal(x))