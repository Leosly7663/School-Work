# Program Name: ComboLockDriver
# Date: 4/1/2022
# Programmer: Leo
# Description: The program to simulate a combination lock storing and receiving combinations

# import random and Dog class from Dog.py
import random
from Dog import Dog

# tell the user the input names and breeds
print("Two dogs will be created please enter their names, and breeds")

# get the users choice of name and breed for dog 1
name1Temp = input("what is the first dogs name?: ")
breed1Temp = input("what is the first dogs breed?: ")

# store the users choice in the Dog class while also generating random variables for age, hunger, and aggressiveness
dog1 = Dog(name1Temp, breed1Temp, random.randrange(0, 14), random.randrange(0, 20), random.randrange(0, 20))

# get the users choice of name and breed for dog 1
name2Temp = input("what is the second dogs name?: ")
breed2Temp = input("what is the second dogs breed?: ")

# store the users choice in the Dog class while also generating random variables for age, hunger, and aggressiveness
dog2 = Dog(name2Temp, breed2Temp, random.randrange(0, 14), random.randrange(0, 20), random.randrange(0, 20))

# ask the user if they'd like to change an aggression value
choice1 = input("Would you like to change a dogs aggression (yes/no)?: ")
if choice1 == "yes":
    # give them the choice of which dog to alter
    choice2 = input("For "+dog1.dogName+" or "+dog2.dogName+"?: ")
    # and what the new value will be
    choice3 = int(input("To what value?: "))
    # save the new value to the corresponding dog
    if choice2 == dog1.dogName:
        dog1.dogAggression = choice3
    elif choice2 == dog2.dogName:
        dog2.dogAggression = choice3

# ask the user if they'd like to change a hunger value
choice1 = input("Would you like to change a dogs hunger (yes/no)?: ")
if choice1 == "yes":
    # give them the choice of which dog to alter
    choice2 = input("For "+dog1.dogName+" or "+dog2.dogName+" ?: ")
    # and what the new value will be
    choice3 = int(input("To what value?: "))
    # save the new value to the corresponding dog
    if choice2 == dog1.dogName:
        dog1.dogHunger = choice3
    elif choice2 == dog2.dogName:
        dog2.dogHunger = choice3

# print the dogs stats and which dog they belong to
print("\n---------------Dog 1-------------------\n" + str(dog1))
print("---------------Dog 2-------------------\n" + str(dog2))

# simulate the interaction in the dog interaction function in the dog class
print(dog1.dog_interaction(dog2))
