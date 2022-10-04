import math
val = int(input("what number would you like to test? "))
valRoot = math.sqrt(val)
valRootSquared = math.pow(valRoot,2)
print("The square root of the square is equal to " + str(valRootSquared))
print("The python math error is equal to " + str(valRootSquared-val))
