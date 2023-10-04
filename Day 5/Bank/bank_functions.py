def_acount_number = 2000001

def create_account(account, account_number, name, password, balance=0, interest_rate=3):
        account.account_number = account_number
        account.name = name
        account.password = password
        account.balance = balance
        account.interest_rate = interest_rate
    
def info(account):
    print("----------------------------------")
    print(f"Acount: {account.account_number}")
    print(f'Name: {account.name}')
    print(f'Balance: {account.balance}')
    print(f'Interest Rate: {account.interest_rate}')
    print("----------------------------------")
    print()

def deposit(account, amount):
    if amount<0:
        print("Invalid Deposit Amount")
    else:
        account.balance+=amount
        print("Amount deposited successfully")
    
    info(account)
    
    
def withdraw(account, amount, password):
    if amount<0:
        print("Invalid Withdrawal Amount")
    elif amount>account.balance:
        print("Withdrawal Amount greater than Balance")
    elif password != account.password:
         print("Incorrect Password")
    else:
        account.balance-=amount
        print("Amount withdrawn successfully")
    info(account)

def transfer(from_account, to_account, amount, password):
    if amount<0:
        print("Invalid Transfer Amount")
    elif amount>from_account.balance:
        print("Transfer Amount greater than Balance")
    elif password != from_account.password:
         print("Incorrect Password")
    else:
        from_account.balance-=amount
        to_account.balance+=amount
        print("Amount transfered successfully")
    print("\n-- From --")
    info(from_account)
    print("-- To --")
    info(to_account)

def credit_interest(account):
    account.balance+=(account.balance*account.interest_rate/1200)
    print('Interest Credited')
    info(account)

def generate_account_number():
     global def_acount_number
     def_acount_number += 1
     return def_acount_number