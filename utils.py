# utils.py
from bank_account import BankAccount
from person import Person
 
def person_data():
    name = input("Enter the person's name:\n")
    new_person = Person(name)
 
    while True:
        account_number = int(input("Enter a 4-digit account number:\n"))
        balance = float(input("Enter the initial balance:\n"))
        new_account = BankAccount(account_number, balance)
        new_person.add_account(new_account)
 
        done = input("Are you done adding accounts? (yes/no):\n")
        if done == "yes":
            break
 
    return new_person
 
def balance_summary(person_list):
    for person in person_list:
        total = 0.0
        for account in person.accounts:
            total = total + account.balance
        print(f"{person.name} : {total:.2f}")