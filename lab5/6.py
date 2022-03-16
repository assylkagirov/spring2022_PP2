import re as regex
txt = input()
print(regex.sub("[ ,.]", ":", txt))