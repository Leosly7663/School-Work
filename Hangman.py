# Program Name: Hangman
# Date: 3/21/2022
# Programmer: Leo
# Description: To play hangman

# need random to select a random word
import random

# list of words separated by category
words = [["hockey game", "home run", "athlete award", "all star"], ["bosnia and herzegovina", "united arab emirates", "ukraine", "canada"], ["ryan reynolds", "scarlett johansson", "dwayne johnson", "jack black"]]
# the categories available
categories = ["sports", "Countries", "Celebrities"]

# the "stages" of the hangman each index is equivalent to that many wrong guesses
stages = ["   O    ", "   O    \n   |\n   | ", "   O    \n  /|\n / | ", "   O    \n  /|\\\n / | \\", "   O    \n  /|\\\n / | \\\n  /\n_/", "   O    \n  /|\\\n / | \\\n  / \\\n_/   \\_\n"]

# empty counter
count = 0

# placeholders to generate a random word
x = random.randrange(0, 2)
y = random.randrange(0, 3)
mysteryWord = str(words[x][y])

# tell the user their category
print("The Category is",categories[x])

# turn the string into a list of characters which will become blanks
mysteryWordStrList = list(mysteryWord)

# list to store the letters already guessed
guessedLetters = []

# empty counter
check = 0

# nested in a while loop to allow for a break when the game is won or lost
while True:
    # print out the blanks
    for w in range(len(mysteryWordStrList)):
        # if the current letter is in your guessed letters then it will not be replaced by a blank
        if mysteryWordStrList[w] in guessedLetters:
            print(mysteryWordStrList[w],end="")
        # if the current letter is actually a space then it is skipped
        elif mysteryWordStrList[w] == " ":
            print(" ",end="")
        # if the letter is not a space or been guessed then it is a blank
        else:
            print("_", end="")
    # new line for neatness
    print("\n")
    # take the users guess of letter
    guess = input("What is your letter guess?: ")
    # add the guess to the list of guessed letters
    guessedLetters.append(guess)

    # counts the amount of correct letters in the word
    for i in range(len(mysteryWordStrList)):
        if mysteryWordStrList[i] in guessedLetters:
            check += 1
    # if you have as many letters correct as there are in the word then you win
    if check == len(mysteryWord.replace(" ","")):
        print("YOU WIN")
        break
    check = 0

    # if the letter exists in the word then the user is told they guessed correctly
    if mysteryWord.find(guess) != -1:
        print("That letter is in the word!")
        continue
    # if the letter is not in the word then count (number of guesses) goes up and a body part is added
    else:
        print(stages[count])
        count += 1

    # if the count reaches 6 then the hangman is complete and you have lost
    if count == 6:
        print("Game Over")
        print("The word was", mysteryWord)
        break



