# Program Name: ComboLockDriver
# Date: 4/1/2022
# Programmer: Leo
# Description: The program to simulate a combination lock storing and receiving combinations

# import the ComboLock class and random
from ComboLock import ComboLock
import random

# tell the users to set their lock
print("You need to set the numbers for your new lock")
# get the lock combination
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# store the combination numbers in the ComboLock class under comboLock1
comboLock1 = ComboLock(num1, num2, num3)
# tell the user their combo has been saved
print("Your combination has been stored\n\nTry to open it!")

# take the users "guess" for the lock combination
num1Guess = int(input("Enter first number: "))
num2Guess = int(input("Enter second number: "))
num3Guess = int(input("Enter third number: "))

# if the comparison stored in the check_combo function returns true then the lock unlocks other wise the lock stays locked
if comboLock1.check_combo(num1Guess, num2Guess, num3Guess):
    print("\nCongratulations! You got the combination right!\nThe lock is now open.")
else:
    print("\nYour guess was incorrect. The lock is still locked.")

# sets a new combination in the ComboLock class under comboLock2 with random numbers from 1-3
comboLock2 = ComboLock(random.randrange(1, 3), random.randrange(1, 3), random.randrange(1, 3))
print("\nA new lock has been randomly generated\nTry to guess its combination")

# create the guesses variable to store the amount of guesses at the combo the user has made
guesses = 0

# while the guesses remain under 3
while guesses < 3:
    # take the users guess at the combination
    num1Guess = int(input("Enter first number (1 - 3): "))
    num2Guess = int(input("Enter second number (1 - 3): "))
    num3Guess = int(input("Enter third number (1 - 3): "))
    # if the user guesses correct then the loop is broken and the user is told the lock is open
    if comboLock2.check_combo(num1Guess, num2Guess, num3Guess):
        print("\nCongratulations! You got the combination right!\nThe lock is now open.")
        break
    else:
        # if the user does not guess the combo then 1 guess is added to the talley and they are told they have x amount of guesses left
        guesses += 1
        print("\nYour guess was incorrect. The lock is still locked.\nYou have", 3-guesses, "guess(es) left")
# if their guesses hit 3 then they are told they have ran out of guesses and the lock has not opened
# they are also told the mystery combination
if guesses == 3:
    print("You have run out of guesses, the lock did not open")
    print(comboLock2)
