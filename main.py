from bank_account import BankAccount
from person import Person
from utils import person_data, balance_summary
 
person_list = []
 
while True:
    print("Choose an option:")
    print("1. Add a new person")
    print("2. Add an account to a person")
    print("3. Show all balances")
    print("4. Quit")
    option = input()
 
    if option == '1':
        new_person = person_data()
        person_list.append(new_person)
 
    elif option == '2':
        name = input("Enter the person's name:\n")
        found = False
        for person in person_list:
            if person.name == name:
                account_number = int(input("Enter a 4-digit account number:\n"))
                balance = float(input("Enter the initial balance:\n"))
                new_account = BankAccount(account_number, balance)
                person.add_account(new_account)
                found = True
                break
        if not found:
            print("Person not found.")
 
    elif option == '3':
        if len(person_list) == 0:
            print("No data to show.")
        else:
            balance_summary(person_list)
 
    elif option == '4':
        print("Goodbye!")
        break
 
    else:
        print("Invalid option. Please choose 1-4.")