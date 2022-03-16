somestr = input('Input a string: ')
print(somestr.lower().replace(' ', '') == ''.join(reversed(somestr.lower().replace(' ', ''))) and 'Palindrome' or 'Not palindrome')