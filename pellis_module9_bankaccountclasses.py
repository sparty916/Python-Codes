#Pj Ellis - Module 9 - Bank Account Class with Inheritence Classes

class BankAccount():
    '''This is Parent Class of my Bank Account'''
    
	#initalizes the object
    def __init__(self, acctid, balance):
        self.acctid = acctid
        self.balance = balance
    
    #will be used to calculate withdrawls    		
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawn amount is negative.")
        if amount > self._balance:
            raise ValueError('Dont have sufficient balance')
        self.balance -= amount
	
	#will be used to calculate deposits
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount is negative.")
        self.balance += amount
	
	#gets the most up to date balance
    def getBalance(self):
        return self.balance


class CheckingAccount(BankAccount):
    '''This is a Child Class of Bank Accoutn for Checking Account'''
   
    #intializes the object with added variables
    def __init__(self, acctid, balance, fees, minBalance):
        super().__init__(acctid, balance)
        self.fees = fees
        self.minBalance = minBalance
        if self.checkMiniBalance():
            self.deductFees()
        else:
            print(f"Your Balance: ${balance:.{2}f}")
	
	#uses to dedudt fees and update the balance		
    def deductFees(self):
        print(f'${self.fees:.{2}f} deducted for not maintaining sufficient balance')
        self.balance -= self.fees
        print(f'Your updated balance is ${self.balance:.{2}f}')
        	
	#checks the minimum balance value against the balance
    def checkMiniBalance(self):
        return self.getBalance() < self.minBalance

class SavingsAccount(BankAccount):
	'''This is my second Child Class of Bank Account for Savings Account'''
	def __init__(self, acctid, balance, interestrate):
		super().__init__(acctid, balance)
		self.interestrate = interestrate
		
	def addInterest(self):
		interest = self.getBalance() * self.interestrate / 100
		self.deposit(interest)

print()
print("Welcome to EllisBank")
print()

def main():
    while True:
        acctid = input('Please Enter Checking Account ID: ')
        balance = float(input('Enter checking account balance: '))
        minbalance = float(input('Enter minimum balance to be maintained: '))
        fees = float(input('Enter fees to be deducted for not maintaining minimum balance: '))
        account1 = CheckingAccount(acctid, balance, fees, minbalance)
        print("\nWould you like to try again?")
        more = input("Press 0 to exit ")
        if more == "0": #to end the loop
            break

main()
