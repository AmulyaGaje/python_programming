# polymorphism
# method overriding-The correct method is invoked at runtime based on the actual type of the object in the list
class Payment:
    def pay(self,amount):
        print("Payement successful")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} in cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using credit/debit card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount}using UPI")
cp=CardPayment()
np=CashPayment()
up=UPIPayment()
p=Payment()
p.pay(88)
li={cp,np,up}
for i in li:
    i.pay(1000)

