# Program Name: Game Of Life
# Date: 3/21/2022
# Programmer: Leo
# Description: To simulate primitive life in python

# need random for the first generation
import random

# create an empty board
board = []

# generate the blank board with periods
for i in range(20):
    board.append([])
    for w in range(20):
        board[i].append(".")

# take the users input on how many cells will start the cycle
startingCells = input("How many cells will you start with?: ")

# randomly place the Os in places that there are not already Os
for i in range(int(startingCells)):
    randRow = random.randrange(0, 19)
    randCol = random.randrange(0, 19)
    # make sure to not place an O where the already is one
    if board[randRow][randCol] != "O":
        board[randRow][randCol] = "O"


# a function to check if the cell will be alive on the next cycle, returns true for life and false for death
def lifeCheck(x,y,status):
    # counts the amount of "alike" cells beside each other
    # for example a dot beside a dot gets +1 count and a O beside an O gets one
    # x and y are the coordinates of the current cell and status is a boolean of alive or dead
    count = 0
    try:
        if board[x][y] == board[x-1][y]:
            count += 1
        else:
            pass
    except IndexError:
        pass
    try:
        if board[x][y] == board[x+1][y]:
            count += 1
    except IndexError:
        pass

    try:
        if board[x][y] == board[x-1][y+1]:
            count += 1
    except IndexError:
        pass

    try:
        if board[x][y] == board[x][y+1]:
            count += 1
    except IndexError:
        pass

    try:
        if board[x][y] == board[x+1][y+1]:
            count += 1
    except IndexError:
        pass

    try:
        if board[x][y] == board[x-1][y-1]:
            count += 1
    except IndexError:
        pass

    try:
        if board[x][y] == board[x][y-1]:
            count += 1
    except IndexError:
        pass

    try:
        if board[x][y] == board[x+1][y-1]:
            count += 1
    except IndexError:
        pass
    # if a dead cell has exactly 5 dead cells beside it then it has 3 living ones and will be born
    if status is False and count == 5:
        # returns true to make the cell alive on the next generation
        return True
    # if a living cell has 3 or 2 living cells beside it then it will continue to live
    elif status is True and (count == 3 or count == 2):
        return True
    # if this requirement is not met then the cell dies or stays dead
    else:
        return False

print("----------Generation 1------------")
# print the first generation board
for i in range(0,19):
    print("".join(board[i]))

# seperator
print()



generations = int(input("How many generations will you have?: "))

for g in range(generations):
    # add two too g because we start on the second generation
    print("----------Generation", g+2, "-----------")
    # run the check of life on each cell
    for i in range(0,19):
        for w in range(0,19):
            # tells the life check what the current status of the cell is
            if board[i][w] == ".":
                status = False
            else:
                status = True
            # if lifecheck returns True then the cell will live
            if lifeCheck(i, w, status):
                board[i][w] = "O"
            # if not then the cell dies
            else:
                board[i][w] = "."
        # print the new board
        print("".join(board[i]))

