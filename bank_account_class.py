class BankAccount(object):
    """A bank account object."""
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'This account belongs to %s, and the balance is %.2f' % (self.name, self.balance)

    def show_balance(self):
        print 'Balance is $%.2f' % (self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print 'You cant deposit 0.'
            return
        else:
            print 'You are depositing %.2f' % amount
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print 'That is not a valid amount for withdrawal'
        elif amount > self.balance:
            print 'You are trying to withdraw %.2f..' % (amount)
            print 'You cant withdraw more than you have (your balance is %.2f).' % (self.balance)
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
my_account.withdraw(3000)
my_account.deposit(0)
print my_account
