import random

numrandom = random.randint(1,20)
print("Hello! What is your name?")
name = input("")
print("Well,", name ,", I am thinking of a number between 1 and 20.")
cnt = 0

def takeaguess(numrandom,name):
    print('Take a guess.')
    num = int(input(''))
    if num < numrandom:
        print("Your guess is too low.")
        return True
    elif num > numrandom:
        print("Your guess is too high.")
        return True
    else:
        print("Good job, ", name, "! You guessed my number in ", cnt + 1 ," guesses!")
        return False

bool = True
while(bool):
    bool = takeaguess(numrandom,name)
    cnt+=1