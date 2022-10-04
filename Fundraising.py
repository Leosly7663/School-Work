# Program Name: Fundraising
# Date: 3/20/2022
# Programmer: Leo
# Description: To store donation information from across the school board

# list of all the schools
SMCDSB = ["St. Joseph\'s", "St. Peter\'s", "St. Joan of Arc", "Holy Trinity", "St. Thomas Aquinas", "Patrick Fogarty", "St. Theresa\'s", "St. Dominics", "Jean Vanier"]
# the options of donation
donationChoices = ["25 Cents", "50 Cents", "1 Dollar", "2 Dollars"]
# empty list to store the 2-D values
donations = []
sum = 0

import math

# create an empty 2-D list to fill with donations
for i in range(len(SMCDSB)):
    donations.append([])
    for w in range(4):
        donations[i].append(0)

# kept in a while loop to allow for multiple entrances, and for exit at any time
while True:
    # print the options list for schools
    print("Which school is collecting a donation?")
    for i in range (9):
        print(i, "-", SMCDSB[i])
    print("9 - Exit")

    # school choice
    school = int(input("School #: "))
    # if the user chooses 9 the program is exited by a break function
    if school == 9:
        break
    # empty line for clarity
    print()

    # print the list of donation choices
    for i in range(4):
        print(i, "-", donationChoices[i])
    # the user may also exit at this point by entering 4
    print("4 - Exit")

    # the user enters their donation choice
    donationAmount = int(input("Donation #: "))
    if donationAmount == 4:
        break

    # take the population of this school
    pop = int(input("What is the school population?: "))

    # save this info under the school and donation catergory
    # the monetary value is equal to the population x 0.25 x 2 ^ the donation choice (ex donation choice 3 is 2^3 or 8 x 0.25 which is 2 dollars)
    donations[school][donationAmount] = pop*0.25*2**donationAmount

    # this is just a spacer to even out the table and prevent rows from being longer than each other
    x = max(donations)
    x = max(x)
    spaces = (len(str(int(x)))-1)/2

    # ask the user if they want to see the chart that is saving their info
    if input("Would you like to see the chart?: ") == "yes":
        # print school acronyms and amount and total
        print("AMT      SJO  |  PET  |  JOA  |  HTR  | STS  |  PFO  |  STH  |  DOM  |  JVA |  TOTAL \n")
        # print the amount column
        for w in range(4):
            if w == 0:
                print((0.25*2**w), end="  ")
            else:
                print((0.25 * 2 ** w), end="   ")
                # adds space depending on the length of the longest # so all columns are even
            for i in range(len(donations)):
                if donations[i][w] == 0:
                    print(" "*math.floor(spaces),end="")
                    print(donations[i][w],end="")
                    print(" "*math.ceil(spaces), end="  |  ")
                else:
                    print(int(donations[i][w]), end="  |  ")
                    # print the sum category
                sum += int(donations[i][w])
            print(sum)
            sum = 0
