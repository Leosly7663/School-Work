# Program Name: Car tester
# Date: 3/25/2022
# Programmer: Leo
# Description: use the car class from car.py to demonstrate an understanding of classes and objects

# import car class
from Car import Car

# assign no values to car 1
car1 = Car()
# assign 4 values to car 2
car2 = Car("Nissan", "Kicks", "2021", "31,430")
# assign 6 values to car 3
car3 = Car("Tesla", "Model 3", "2020", "42,880", "Electric", "Electric")

# print the car number
print("------ Car 1 ------")
# print the car information for car 1
print(car1)
# print the car number
print("------ Car 2 ------")
# print the car information for car 2
print(car2)
# print the car number
print("------ Car 3 ------")
# print the car information for car 3
print(car3)
# car 3 honk
print("Car 3 says:")
# run the car horn function for car 3
car3.carHorn()
