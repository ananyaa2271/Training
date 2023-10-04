import account as bank
import bank_functions as functions

def main():

    user_1 = bank.Account()
    functions.create_account(user_1, functions.generate_account_number(), 'John', '1234567890')
    functions.deposit(user_1, 5100)

    user_2 = bank.Account()
    functions.create_account(user_2, functions.generate_account_number(), 'Harry', '9876543210')
    functions.deposit(user_2, 10000)


    functions.transfer(user_2, user_1, 2500, '9876543210')

    functions.credit_interest(user_1)

    functions.withdraw(user_1, 7000, '1234567890')

    functions.deposit(user_1, 10000)


main()