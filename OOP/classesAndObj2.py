class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def debit(self, amount):
        self.bal = self.bal - amount
        print('Rs. ',amount, ' debited')
        print('Remaining balance is : Rs. ',self.balance())

    def credit(self, amount):
        self.bal = self.bal + amount
        print('Rs. ', amount, ' Credited')
        print('Remaining balance is : Rs. ', self.balance())

    def balance(self):
        return self.bal

a1 = Account(50000, 12345)
a1.debit(5000)
a1.credit(20000)