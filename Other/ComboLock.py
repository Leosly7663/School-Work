# Program Name: ComboLock
# Date: 4/1/2022
# Programmer: Leo
# Description: Store Class information for the ComboLockDriver program

# create the combo lock class
class ComboLock:
    # assign default values
    def __init__(self, num1=0, num2=0, num3=0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    # a function to check if the 3 numbers guessed are the same as the three numbers stored
    def check_combo(self, num1guess, num2guess, num3guess):
        if self.num1 == num1guess and self.num2 == num2guess and self.num3 == num3guess:
            # returns True if the lock unlocks
            return True
        else:
            # returns false if the lock does not unlock
            return False

    def __str__(self):
        # defines and returns the actual combination
        output = "The combination is "+ str(self.num1) + "," + str(self.num2) + "," + str(self.num3)
        return output

