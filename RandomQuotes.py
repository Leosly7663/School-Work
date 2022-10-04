# Program Name: Random Quotes
# Date: 4/8/2022
# Programmer: Leo
# Description: A program that will read quotes from a file and print a random one

# import random to randomly assign a quote
import random

# empty list to fill with quotes from the file
quotes = []
# the name of the file full of quotes
fileName = "quotes.txt"

# try to open the file
try:
    # open the file with the given name
    myFile = open(fileName,"r")
    # loops through each line in myFile
    for myLine in myFile:
        # append each quote to the list
        quotes.append(myLine)
    # close the file
    myFile.close()
# if file is invalid tell the user
except IOError:
    print("Invalid File")

# pick a random number from 0 to the amount of quotes in the list
num = random.randrange(0, len(quotes)-1)

# print the quote associated with the random number
print(quotes[num])
