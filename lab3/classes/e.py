class Account:
    owner = ''
    balance = 0.0
    def init(self, name):
        self.owner = name
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Current balance:", self.balance)
    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("You do not have enough money")
        else:
            self.balance = self.balance - amount
            print("Current balance:", self.balance)

name = input("Set a name: ")
acc = Account(name)
bool = True
while(bool):
    print("D[Deposit], W[Withdraw], Any other[Exit]")
    cmd = input()
    if cmd == "D":
        acc.deposit(float(input("How much do you wanna deposit: ")))
    elif cmd == "W":
        acc.withdraw(float(input("How much do you wanna withdraw: ")))
    else:
        bool = False