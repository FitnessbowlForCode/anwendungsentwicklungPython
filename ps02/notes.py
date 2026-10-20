class account():
    def __init__(self, owner = "owner", balance = 0, kn = 111):
        self.owner = owner
        self.balance = balance
        self.kn = kn

    def __str__(self):
        return"{} {} {}".format(self.owner, self.balance, self.kn)

    def plus (self, x):
        self.x = x
        self.balance += x

    def minus(self, x):
        self.x = x
        self.balance -= x

a1 = account("Alex")
print(a1)

a1.plus(10)
print(a1)

a1.minus(20)
print(a1)