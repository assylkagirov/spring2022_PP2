def revresen(sen):
    
    words = sen.split(' ')
    string =[]
    for word in words:
        string.insert(0, word)
    return string
 
sen = str(input())
print(' '.join(revresen(sen)))