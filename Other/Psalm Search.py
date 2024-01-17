# Program Name: Psalm Search
# Date: 4/30/2022
# Programmer: Leo
# Description: Introduction to sorting algorithms in python

import math

# open the file of psalms to be searched from
psalmsText = open("Psalms.txt", "r")

# empty lists to be filled
e = []
d = []
g = []
count = 0

# for every even line save the line to e and for every odd line save it to d
for i in psalmsText:
    if count % 2 == 0:
        e.append(i.strip("\n"))
    else:
        d.append(i.strip("\n"))
    count += 1

# turn the list of strings into numbers
for i in e:
    g.append(int(i))

e = [1, 2, 4, 7, 8, 12, 16, 18, 22, 23, 26, 29, 33, 37, 40, 44, 49, 58, 63, 68, 71, 81, 86, 94]

# ask the user for their choice of Psalm
psalmNumber = int(input("What Psalm are you looking for?: "))

# the primary search function
def bin_search(check, w):
    #
    # print functions to show the process
    print(w[int(len(w) / 2)])
    print(w)
    #
    # if the middle number is equal to the number we are looking for then it has been found
    if w[int(len(w) / 2)] == check:
        w = check
        return w

    # if the middle number does not equal the number we are looking for
    elif w[int(len(w) / 2)] != check:
        # if the middle number is bigger than the number we are looking for
        if w[int(len(w) / 2)] < check:
            # delete the first half of numbers
            del w[:int(math.ceil(len(w) / 2))]
            return w
        # if the middle number is greater than the number we are looking for
        elif w[int(len(w) / 2)] > check:
            # if the middle number does not equal 1 (this causes the item to be deleted)
            if int(len(w) / 2) != 1:
                # delete the last half of the numbers
                del w[-int(math.floor(len(w) / 2)):]
            return w


def bin_check(w, check):
    # if the length of the list has been reduced to 1
    if len(w) == 1:
        # if the middle number is the number we are looking for (in a list of 1)
        if w[int(len(w) / 2)] == check:
            # tell the user their number appears in the list and print the corresponding psalm
            print(str(x), "does exist in the list")
            print(d[e.index(x[0])])
        # if the middle number is not equal to the number we are looking for
        elif w[int(len(w) / 2)] != check:
            # tell the user their number is not where in the list
            print(str(x), "does NOT exist in the list")


# call the first binary search
x = bin_search(psalmNumber, g)

# continue to search until the list is reduced to 1
while True:
    x = bin_search(psalmNumber, x)
    try:
        # if the length is one then run the bin_check to print the proper results
        if len(x) == 1:
            bin_check(x, psalmNumber)
            break
    # if the middle value was the number we were looking for before the list was reduced to 1
    except TypeError:
        # print that the number has been found and its corresponding psalm
        print(str(x), "does exist in the list")
        print(d[e.index(x)])
        break

