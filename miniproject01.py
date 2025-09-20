class banker:
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"the amount deposit is{amount}")
        else:
            print("enter positive num okay babe;")
    def withdraw(self,withdraw):
        if withdraw>0 and withdraw<self.balance:
            self.balance-=withdraw
            print(f"the amouny withdraw is {withdraw}")
        else:
            print("enter valid amount:okay babe")      
    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")

# Example usage:
account1 = banker("Abdullah", 1000)
account1.check_balance()

account1.deposit(500)
account1.withdraw(300)
account1.check_balance()        
 
    
        
        