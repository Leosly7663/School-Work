# Program Name: Car
# Date: 3/25/2022
# Programmer: Leo
# Description: store the car class for the car tester program

# create the class
class Car:
    # The default car values for unentered info
    def __init__(self, make="Ford", model="Focus", year="20XX", price="X$", engine="v8", gasTankSize="36L"):
        # assign the variables
        self.carMake = make
        self.carModel = model
        self.carYear = year
        self.carPrice = price
        self.carEngine = engine
        self.carGasTankSize = gasTankSize

    # car horn function returns Honk! Honk! when called
    def carHorn(self):
        print("Honk! Honk!")

    # print out car information for the car referenced
    def __str__(self):
        output = "Make: " + self.carMake + "\n"
        output += "Model: " + self.carModel + "\n"
        output += "Year: " + str(self.carYear) + "\n"
        output += "Price: " + str(self.carPrice) + "\n"
        output += "Engine: " + str(self.carEngine) + "\n"
        output += "The size of the gas tank is: " + str(self.carGasTankSize)
        # output string is complete, return it
        return output
