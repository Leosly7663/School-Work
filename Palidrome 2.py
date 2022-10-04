# Program Name: Palindrome 2
# Date: 2/28/2022
# Programmer: Leo
# Description: To evaluate if a users sentence input contains a valid palindrome or not

# put the old palindrome code in a for loop for every word in the sentence
userSentence = input("enter your sentence to check for palindromes: ")
palSentence = list(userSentence.split())
# empty list to be filled with palindromes
outputList = []
for w in range(len(palSentence)):
    # replace the user inputted word with a word from the sentence (from the list)
    userPal = palSentence[w]

    # simplify the users input into all lowercase for easy evaluation
    palLower = userPal.lower()

    # the last indexable value becomes the first and the first the last, the second becomes the second last ect...
    # we take the length and subtract 1 to get our "last" value
    lengthPal = len(palLower)-1

    # change str into a list of characters
    palList = list(palLower)
    # a loop that replaces the palLower[i] with the palLower[lengthPal-i] until the loop reaches half the length of the word

    for i in range(0, int(lengthPal+1/2)):
        start = palList[i]
        end = palList[lengthPal-i]
        palList[i] = end
        palList[lengthPal-i] = start

    # joins the character items of the list into a word
    palReversed = "".join(palList)

    # if the reversed word is the same as the word forwards then the user is told its a palindrome!
    if palReversed == palLower:
        # add the palindrome to a list to be printed at the end
        outputList.append(palLower)
    # else the reversed word is NOT the same as the word forwards and is not added to the output


print("There are ", len(outputList), " palindromes in this sentence")
print("The palindromes in this sentence are: ", ", ".join(outputList))
