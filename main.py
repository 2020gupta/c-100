class Atm:
    def __init__(self,card,pin):
        self.card=card
        self.pin=pin
    def checkBalance(self):
        print("your balance is 50000")
    def cashwithdrawal(self,amount):
        new_amount=50000-amount
        print("you have withdrawn"+str(amount))
        print("your balance is "+str(new_amount))
def main():
    card=input("enter card number")
    pin=input("enter yur pin")
    user=Atm(card,pin)
    print("choose your activity")
    print("1=balance enquiry,2=withdrawal")
    activity=int(input("enter your activity"))
    if activity==1:
        user.checkBalance()
    elif activity==2:
        amount=int(input("enter amount"))
        user.cashwithdrawal(amount)
    else:
        print("enter valid number")
main()