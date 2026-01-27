
class BankAccount:
    ROI=10.0
    def __init__(self,name,amount):
       self.Name=name
       self.Amount=amount
        

    def Display(self):
        print("Account Holder: ",self.Name)
        print("Current Balance: ",self.Amount)
        
    def Deposit(self):
        amt =float(input("Enter amount to deposit: "))
        self.Amount += amt

    def Withdraw(self):
        amt=float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient balance")
   

    def CalculateInterest(self):
        interest =(self.Amount * BankAccount.ROI)/100
        return interest

   
obj1 = BankAccount("ABC",10000)
obj2 = BankAccount("XYZ",3000)

print("Account 1")
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest is: ",obj1.CalculateInterest())
obj1.Display()

print("--------------------")
print("Account 2")
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
print("Interest is: ",obj2.CalculateInterest())
obj2.Display()


