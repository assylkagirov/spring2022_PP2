def palindrome(word):
    if word == word[::-1]:
        print("its palindrom")
    else:
        print("its not palindrom")
    
word = str(input())
palindrome(word)
