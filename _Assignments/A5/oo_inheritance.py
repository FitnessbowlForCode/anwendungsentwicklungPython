### Assignment oo_inheritance ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO

####### IMPORTANT #######

# Make sure your document doesn't contain any syntax error and contains all procedures

#########################



# Implement the whole functionality for this assignment in this file!
# Modify and add to the provided code!

class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Ungültige Eingabe!")

    def withdraw(self, amount: float):
        if amount > 0:
            self.__balance -= amount
        else:
            raise ValueError("Ungültige Eingabe!")

    def __str__(self):
        return f"Account(owner='{self.owner}', balance={self.__balance} €)"

    @staticmethod
    def transfer(amount: float, a, b):
        a.withdraw(amount)
        b.deposit(amount)

    @property
    def balance(self):
        return self.__balance


class StudentAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Startguthaben darf nicht negativ sein!")
        super().__init__(owner, balance)

    def withdraw(self, amount: float):
        if self.balance - amount < 0:
            raise ValueError("Nicht genug Guthaben!")
        super().withdraw(amount)                  

##############################################

a1 = Account("A")
#print(type(a1.owner))
#print(type(a1.balance))

a2 = Account("B")

a1.deposit(100)

a2.withdraw(100)    

print(a1)
print(a2)

Account.transfer(600, a1, a2)

print(a1)
print(a2)

print(a1.owner)
print(a1.balance)

#a1.balance = 999   ##this should not be allowed! Note: Geht auch nicht. Bräuchte man einen balance.setter

s1 = StudentAccount("S")
s1.deposit(100)
print(s1)
print(s1.balance)

try:
  Account.transfer(500000, s1, a1)
except:
  print("Fehler") ##TODO where should the error message come from?

print(s1)
print(a1)

'''
##################### Demo ############

a1 = Account("A")
a2 = Account("B")
a1.deposit(100)
a2.withdraw(100)
print(a1)
print(a2)
Account.transfer(600, a1, a2)
print(a1)
print(a2)

print(a1.owner)
print(a1.balance)

#a1.balance = 999   ##this should not be allowed!

s1 = StudentAccount("S")
s1.deposit(100)

try:
  Account.transfer(500000, s1, a1)
except:
  print("Fehler") ##TODO where should the error message come from?
print(s1)
print(a1)
'''