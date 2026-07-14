class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
        

    def Display(self):
        print(self.Name,"current balance",self.Amount)

    def Deposit(self):
        money=int(input("enter amount to Deposit :"))
        self.Amount=self.Amount + money

    def withdraw(self):
        money=int(input("enter amount to Deposit :"))
        self.Amount=self.Amount - money
        
    def CalculateIntrest(self):
        Intrest = (self.Amount * BankAccount.ROI) / 100
        return Intrest

obj1 = BankAccount("Tanvi", 10000)

obj1.Display()
obj1.Deposit()
obj1.Display()
obj1.withdraw()
obj1.Display()

print("Interest:", obj1.CalculateIntrest())
