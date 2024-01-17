# Program Name: ATM_data
# Date: 3/25/2022
# Programmer: Leo
# Description: File containing the ATM class used in ATM.py

class ATM:
    # preset bank and balance info
    def __init__(self, bank="Unknown", balance=0):
        # assign values
        self.atmBank = bank
        self.atmBalance = balance

    # the add interest function used to calculate and add interset to balance
    def addIntrest(self, intrest, period):
        # keeps the user from giving a negative time or percent
        if intrest > 0 or period > 0:
            # balance = balance times interest formula rounded to 2 decimal places
            self.atmBalance = round(self.atmBalance * (1+intrest)**period,2)
        else:
            # tell the user to re-input a value
            return print("Please enter a valid number")

    # the function to add a value to the running balance given an amount
    def addToBalance(self, amount):
        # keeps the user from entering a negative number
        if amount > 0:
            self.atmBalance += amount
        else:
            return print("Please enter a valid number")

    # the function to remove a value to the running balance given an amount
    def removeFromBalance(self, amount):
        # prevents the user from entering a negative number
        if amount > 0:
            self.atmBalance -= amount
        else:
            return print("Please enter a valid number")

    def __str__(self):
        # the options menu
        output = "Please select an option from the following menu" + "\n"
        output += "1: Display Balance" + "\n"
        output += "2: Deposit Money" + "\n"
        output += "3: Withdraw Money " + "\n"
        output += "4: Add Daily Interest" + "\n"
        output += "5: Exit"
        # output string is complete, return it
        return output
