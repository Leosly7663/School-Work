# Program Name: resistors
# Date: 3/04/2022
# Programmer: Leo
# Description: To calculate the resistance value of a given resistor

# dictionary containing the resistor values
resistors = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

# get the users input and convert it into lowercase
# test input is red-BLUE-brown
print("What are the colors of your resistor?")
colors = input("separate each color with a hyphen \"-\": ")
colors = colors.lower()

# split the colors from the input string in a list with - as the separator
colorsList = colors.split("-")

# empty list to store the result
result = []

# start at 0 loop 3 times for indexing
for i in range(0,3):
    # the band value = "blue" = 6 by indexing the dictionary
    bandVal = resistors[colorsList[i]]
    # the first two bands are just the corresponding band value
    if i < 2:
        result.append(bandVal)
    # the last band is 10 to the power of the band value
    else:
        result.append(10**bandVal)

# the first band is multiplied by ten because bands don't work like 9+6 but rather 96 or 9*10 + 6
# this result is then multiplied by the last band to give the resistance value
resultVal = (result[0]*10 + result[1])*result[2]

# print the results
print("you entered:", colors)
print("The value of the resistor is", resultVal, "ohms")
