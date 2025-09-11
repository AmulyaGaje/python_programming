class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Deposited Successfully")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawn successfully")
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
class SBI(BankAccount):
    def display(self):
        print(super().__balance)
s=SBI(1000)
s.display()
b1=BankAccount(0)
b1.deposit(5000)
b1.withdraw(2000)
print("The current balance is",b1.get_balance())
