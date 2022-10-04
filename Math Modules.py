# Program Name: Math Modules
# Date: 2/18/2022
# Programmer: Leo
# Description: To demonstrate an understanding of python math modules

import math

# a logarithum can be used to determine a population over a given period of time and a rate of growth.
# population of 2000 growing at a rate of 1.5% per year
new = int(input("what is your goal population? (over 2000) "))
old = 2000
growth = 0.015
years = math.log(new/old)/math.log(growth+1)

print("") # line break for nice output :)
print("In " + str(years) + " years you will have " + str(new) + " people")

print("")
print(str(years) + " is a very ugly number so lets us math.round to give a nice even number")

# math.round is used to repersent data that does not require all possible decial numbers
print("")
print("In " + str(round(years)) + " years you will have " + str(new) + " people")

##############################################################
input("") # empty input to hold consol to talk
##############################################################

# sin law calc
# sin A / a = sin B / b

a = int(input("How long is side 1? "))
b = int(input("How long is side 2? "))

angleADeg = int(input("what is the angle of A? "))
angleARad = angleADeg * (math.pi/180)

try:
    sinA = math.sin(angleARad)
    angleBDeg = math.asin(sinA*(b/a)) * 180/math.pi
    c = math.sqrt(a**2 + b**2)
    angleCDeg = 180-angleADeg - angleBDeg
    print('''
    Angle a is: ''' + str(angleADeg) + '''
    Angle b is: ''' + str(round(angleBDeg)) + '''
    Angle c is: ''' + str(round(angleCDeg)) + '''
    Side a is: ''' + str(a) + '''
    Side b is: ''' + str(b) + '''
    Side c is: ''' + str(round(c, 2)) + '''
          ''')
except ValueError:
    print("no possible solution")

