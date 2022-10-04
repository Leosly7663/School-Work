year = int(input("What year would you like to check? "))

a = int(year / 100)
b = year % 100
c = int((3*(a+25))/4)
d = 3*(a+25) % 4
q = int((8*(a+11))/25)
f = (5*a+b) % 19
g = (19*f+c-q) % 30
h = int((f+11*g)/319)
j = int((60*(5-d)+b)/4)
k = (60*(5-d)+b) % 4
n = (2*j-k-g+h) % 7
p = (g-h+n+114) % 31
month = int((g-h+n+114)/31)
day = p+1

if month == 4:
    monthStr = "April"
else:
    monthStr = "March"

if day % 10 == 1 and day != 11:
    sufix = "st"
elif day % 10 == 2 and day != 12:
    sufix = "nd"
elif day % 10 == 3 and day != 13:
    sufix = "rd"
else:
    sufix = "th"

print("Easter will take place on Sunday the " + str(day) + sufix + " of " + monthStr + " " + str(year))