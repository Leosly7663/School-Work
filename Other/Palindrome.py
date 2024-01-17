# Program Name: Palindrome
# Date: 2/28/2022
# Programmer: Leo
# Description: To evaluate if a user input is a valid palindrome or not
import math

# the palindrome inputted by the user
userPal = input("What is your palindrome?: ")

# simplify the users input into all lowercase for easy evaluation
palLower = userPal.lower()

# the last indexable value becomes the first and the first the last, the second becomes the second last ect...
# we take the length and subtract 1 to get our "last" value
lengthPal = len(palLower)-1

# change str into a list of characters
palList = list(palLower)
# a loop that replaces the palLower[i] with the palLower[lengthPal-i] until the loop reaches half the length of the word

# 1 is added to lengthPal because it is the indexable length and not the number of letters
for i in range(0, int(lengthPal+1/2)):
    start = palList[i]
    end = palList[lengthPal-i]
    palList[i] = end
    palList[lengthPal-i] = start

# joins the character items of the list into a word
palReversed = "".join(palList)
# prints the word reversed and the original word
print(palLower, "backwards is", palReversed)

# if the reversed word is the same as the word forwards then the user is told its a palindrome!
if palReversed == palLower:
    print(palLower, "is a palindrome!")
# else the reversed word is NOT the same as the word forwards then the user is told its NOT a palindrome!
else:
    print(palLower, "is a NOT palindrome!")
