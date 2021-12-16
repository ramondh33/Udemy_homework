# Create a class with two attributes
class Account():
    
    # Creating Init to associate parameters
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    # Creating functions to see balance
    def accBalance(self):
        print(f"Your balance is {self.balance}")
        
    # Creating functions to update balance based on deposit amount    
    def deposit(self,depositAmount):
        self.balance = self.balance + depositAmount
        print(f"Your new balance is {self.balance}.")
    
    # Creating functions to update balance based on withdrawal amount    
    def withdrawal(self,withdraw):
        
        # If statement checking if funds are available to withdrawal
        if withdraw > self.balance:
            print("Insufficient Funds!")
         
         # Updating balance amount 
        else:  
            self.balance = self.balance - withdraw
            print(f"Your new balance is {self.balance}")
        
accountOne = Account("Jose", 100)

print(f"Account Name: {accountOne.name}\nAccount Balance: ${accountOne.balance}")

depositAmount = int(input("Enter a deposit amount: "))
accountOne.deposit(depositAmount)

withdraw = int(input("Enter amount to withdraw: "))
accountOne.withdrawal(withdraw)

print(accountOne.balance)