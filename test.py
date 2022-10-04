import random

res = [random.randrange(0, 1000, 1) for i in range(int(input("How many numbers do you want in the list?: ")))]

print(res)