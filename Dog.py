# Program Name: Dog
# Date: 4/1/2022
# Programmer: Leo
# Description: Store Class information for the TwoDogsMeet program

# random for random values
import random

# create the class
class Dog:
    # give the dog default values if ones are forgotten
    def __init__(self, name="Unknown", breed="Unknown", age=random.randrange(0, 14), aggression=random.randrange(0, 20), hunger=random.randrange(0, 20)):
        # assign the variables
        self.dogName = name
        self.dogBreed = breed
        self.dogAge = age
        self.dogAggression = aggression
        self.dogHunger = hunger


    # function to simulate a meeting between the two dogs
    def dog_interaction(self, dog2):
        # if current dog aggression is higher than 5 and the other dogs aggression is lower than 5
        if self.dogAggression > 5 > dog2.dogAggression:
            # current dog will growl at other dog
            output = self.dogName + " growls at " + dog2.dogName
            # if current dog hunger is higher than 7 and the other dogs hunger is lower than 7
            output += "\nGRRRRRRR"
            if self.dogHunger > 7 > dog2.dogHunger:
                # if dog is hungry and aggressive then it will bite the other dog
                output += "\n" + self.dogName + " bites " + dog2.dogName
                output += "\n" + dog2.dogName + " runs away from " + self.dogName
        elif self.dogAggression < 5 < dog2.dogAggression:
            # other dog will growl at dog 1
            output = dog2.dogName + " growls at " + self.dogName
            output += "\nGRRRRRRR"
            if self.dogHunger < 7 < dog2.dogHunger:
                # if dog is hungry and aggressive then it will bite the other dog
                output += "\n" + dog2.dogName + " bites " + self.dogName
                output += "\n" + self.dogName + " runs away from " + dog2.dogName
        elif self.dogAggression > 5 < dog2.dogAggression:
            # both dogs growl at each other
            output = "Both dogs growl at each other"
            output += "\nGRRRRRRR"
            if self.dogHunger > 7 < dog2.dogHunger:
                # if dog is hungry and aggressive then it will bite the other dog
                output += "\nBoth dogs snap at each other"
                output += "\nOne of the owners steps in"
                output += "\nThe dogs are separated and given some food, PHEW that was close"
        else:
            # friendly interaction
            output = "The dogs play friendly together"

        # return the created output
        return output

    # the dogs information to be printed when function is called
    def __str__(self):
        output = "Name: " + self.dogName + "\n"
        output += "Breed: " + self.dogBreed + "\n"
        output += "Age: " + str(self.dogAge) + "\n"
        output += "Aggression: " + str(self.dogAggression) + "\n"
        output += "Hunger: " + str(self.dogHunger) + "\n"
        return output
    