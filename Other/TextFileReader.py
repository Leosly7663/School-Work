# Program Name: Text File Reader
# Date: 4/8/2022
# Programmer: Leo
# Description: A simple program that will open a file of the users choice

# assign empty value of none to be reassigned by user
myFile = None

# ask the user what file they would like to open
fileName = input("What is the name of your file?: ")

# try to open the file but expect a IOError
try:
    # open the users file
    myFile = open(fileName,"r")
    # loops through each line in myFile
    for myLine in myFile:
        # print the lines of the file, but do not add extra newlines
        print(myLine, end='')
    # close the file
    myFile.close()
# if file is not valid tell the user
except IOError:
    print("The file inputted does not exist")
