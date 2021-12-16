# Create a class with two attributes
class Account():

# Creating Init to associate parameters
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# Creating functions to see balance
    def Account_Balance(self):
        print(f"Your balance is {self.balance}")

# Creating functions to update balance based on Deposit amount    
    def Deposit(self,depAmount):
        self.balance = self.balance + depAmount

        print(f"Your new balance is {self.balance}.")

# Creating functions to update balance based on Withdrawal amount    
    def Withdrawal(self,withdraw):

# If statement checking if funds are available to Withdrawal
        if withdraw > self.balance:
            print("Insufficient Funds!")

# Updating balance amount 
        else:  
            self.balance = self.balance - withdraw
            print(f"Your new balance is {self.balance}")

accountOne = Account("Jose", 100)

print(f"Account Name: {accountOne.name}\nAccount Balance: ${accountOne.balance}")
depAmount = int(input("Enter a Deposit amount: "))
accountOne.Deposit(depAmount)

withdraw = int(input("Enter amount to withdraw: "))
accountOne.Withdrawal(withdraw)

