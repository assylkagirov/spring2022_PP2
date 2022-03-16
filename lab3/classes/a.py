class newclass():
    def __init__(self):
        self.inputstr = ""

    def get_String(self):
        self.inputstr = input()

    def print_String(self):
        print(self.inputstr.upper())
        
str1 = newclass()
str1.get_String()
str1.print_String()