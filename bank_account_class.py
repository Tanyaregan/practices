class BankAccount(object):
    """A bank account object."""


    def __init__(self, name):
        self.name = name
        self.balance = 0

    def __repr__(self):
        print 'This account belongs to %s, and the balance is %.2f' % (name, balance)

    def show_balance(self):
        print 'Balance is $%.2f' % (self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print 'You need to deposit more than 0'
            return
        else:
            print 'You are depositing %.2f' % amount
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print 'That is not a valid amount for withdrawal'
        elif amount > self.balance:
            print 'You cant withdraw more than you have'
            return
        else:
            print 'You are withdrawing %.2f' % amount
            self.balance -= amount
            self.show_balance()


my_account = BankAccount('Tanya')
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
