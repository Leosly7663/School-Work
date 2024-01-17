# Program Name: ATM
# Date: 3/25/2022
# Programmer: Leo
# Description: Simulate a ATM machine

# import the ATM class and variables to be used in the ATM simulation
from ATM_data import ATM

# assign ATM
atm = ATM()

# save your bank under atm.bank
atm.atmBank = input("What bank do you use?: ")

# nested in while loop to allow for exiting
while True:
    # empty line for neatness
    print()
    # prints the list of menu options
    print(atm)
    # takes the users input fof the menu
    choice = input("")
    # if logic for each menu option
    if choice == "1":
        # displays atm balance
        print("Your current balance is: " + str(round(atm.atmBalance,2)) + "$")
    elif choice == "2":
        # take deposit amount and call add to balance function to add it to the atm balance
        amount = int(input("How much will you deposit?: "))
        atm.addToBalance(amount)
    elif choice == "3":
        # take a withdraw amount and call the remove from balance function to remove the number from the balance
        amount = int(input("How much will you deposit?: "))
        atm.removeFromBalance(amount)
    elif choice == "4":
        # take the interest and period for daily interest
        # divide # by 100 to convert into decimal
        interest = float(input("Please provide interest %: "))/100
        # divide by 365 to convert from daily to annual interest periods
        period = float(input("Please provide days of accumulation: "))/365
        # call the interest function to add the interest to the balance
        atm.addIntrest(interest, period)
    # allow for an option to escape the loop and end ATM simulation
    elif choice == "5":
        break
    else:
        # repeats the loop if the value is not 1-5
        print("Pleas enter a valid input from the list")
        continue
