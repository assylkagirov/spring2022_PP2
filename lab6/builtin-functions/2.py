somestr = input('Input a string: ')
upper, lower = 0, 0
for a in somestr:
    if a.isupper():
        upper += 1
    elif a.islower():
        lower += 1
print('Upper:', upper, '\nLower:', lower)