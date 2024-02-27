# class name should be in pascal case eg. ThisIsPascalCase
# variable and function name in snake case eg.This_is_snake_case
# camel case eg. thisIsPascalCase  
class Atm:
    def __init__(self):  #put space between def and __init and init is constructor  

        self.pin = ""
        self.balance =0
        self.menu()

# self is the current object
# one class function doesn't call other class function
    def menu(self):
        user_input = input("""hello, how would you like to procedd?
                                1. Enter 1 to create pin
                                2. Enter 2 to deposit
                                3. Enter 3 to withdraw
                                4. Enter 4 to check balance 
                                5. Enter 5 to exit
                            """)

        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input =='4':
            self.check_balance()
        else:
            print('bye')
    
    def create_pin(self):
        self.pin = input('Enter your pin')
        print('pin set successfully')
    
    def deposit(self):
        temp = input('Enter your pin')
        if temp == self.pin:
            amount = int(input('Enter the amount'))
            self.balance = self.balance + amount
            print('Deposit Successful')
        else:
            print('Invalid pin')
    
    def withdraw(self):
        temp = input('Enter your pin')
        if temp == self.pin:
            amount = int(input('Enter the amount'))
            if amount<self.balance:
                self.balance = self.balance-amount
                print('Operation Successful')
            else:
                print('invalid pin')
    def check_balance(self):
        temp = input('Enter your pin')
        if temp == self.pin:
            print(self.balance)
        else:
            print('invalid pin')
# instance variable are the variable which is made 
# under the constructor and its value is different for every object.
