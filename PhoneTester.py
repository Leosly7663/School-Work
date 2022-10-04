# PhoneTester.py

from CellPhone import CellPhone

p1 = CellPhone()
p1.carrier = "Rogers"
p1.type = "Samsung Galaxy S10"
p1.speed = 1.2
p1.memory = 12.0
p1.num_apps = 10

p2 = CellPhone()
p2.carrier = input("What is your cellphone carrier?: ")
p2.type = input("What is your cellphone type?: ")
p2.speed = int(input("What is your cellphone speed?: "))
p2.memory = int(input("What is your cellphone memory?: "))
p2.num_apps = int(input("How many apps do you have on your phone?: "))

print()

print("Phone 1")
print("Carrier = " + p1.carrier)
print("Type of phone = " + p1.type)
print("Speed of phone = " + str(p1.speed) + "Ghz")
print("Memory = " + str(p1.memory) + "Gb")
print("Number of Apps = " + str(p1.num_apps))

print()

print("Phone 2")
print("Carrier = " + p2.carrier)
print("Type of phone = " + p2.type)
print("Speed of phone = " + str(p2.speed) + "Ghz")
print("Memory = " + str(p2.memory) + "Gb")
print("Number of Apps = " + str(p2.num_apps))

