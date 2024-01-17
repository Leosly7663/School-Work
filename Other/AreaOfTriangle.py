import math
choice = int(input("would you like to use formula 1 or formula 2? "))

if choice == 1:
    a = int(input("what length will side a be? "))
    b = int(input("what length will side b be? "))
    c = int(input("what length will side c be? "))
    s = (a + b + c) /2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is " + str(area) + " when the side lengths are " + str(a) + " and " + str(
        b) + " and " + str(c))
elif choice == 2:
    a = int(input("what length will side a be? "))
    b = int(input("what length will side b be? "))
    C = int(input("what angle will angle C be? "))
    s = (a + b + C) /2
    area = (a*b*math.sin(C*math.pi/180))/2
    print("The area of the triangle is " + str(area) + " when the side lengths are " + str(a) + " and " + str(
        b) + " and the angle is " + str(C))
else:
    print("Please try again")

