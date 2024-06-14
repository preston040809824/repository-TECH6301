#To create a class called Bank_account
class Bank_account:
    def __init__(self):       
        self.name
        self.account_num
        self.balance=0
        self.customers={}

#To create a new account
    def create_account(self, account_number, name, initial_balance=0):
        if account_number, in self.customers:
            print("Account number already exists.")
        if name in self.customers:
            print("Customer already exists.")
        else:
            self.customers[account_number, name] = initial_balance
            print("Account successfully created.")

 #To deposit funds into bank account   
    def deposit(self, account_number, amount):
        if account_number in self.customers:
            amount=float(input("Please enter deposit amount: "))
        self.customers += amount
        print("Amount deposited:", amount)

#To withdraw funds from bank account
    def withdraw(self, account_number, amount):
        amount=float(input("Please enter amount to be withdrawn: "))
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawn: ", amount)
            else:
                print("Insufficient funds")
        else:
            print("Account number not found.")

#To display balance of funds in bank account 
    def display_bal(self, account_number):
        if account_number in self.customers:
            balance= self.customers[account_number]
            print(f"Balance available: {balance}")
        else:
            print("Account number not found.")

#To display customer account info    
    def display_info(self):
        print("Account holder name: ", self.name)
        print("Account number: ", self.account_num)


#Variables
s=Bank_account()
s.deposit()
s.withdraw()
s.display_bal()
s.display_info()