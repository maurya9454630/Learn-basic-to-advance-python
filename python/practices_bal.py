# Create Account class with 2 attributes - balance & account no.
# Create methods for debit,credit & printing the balance.

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

        pass
    # debit method 
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ",self.get_balance())

            # credit method 
    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credit")
        print("Total balance = ",self.get_balance())


    def get_balance(self):
        return self.balance

acc1 = Account(10000, 123090)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
# print(acc1.balance)
# print(acc1.account_no)