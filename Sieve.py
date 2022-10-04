# Program Name: Sieve
# Date: 3/03/2022
# Programmer: Leo
# Description: To use python lists and logic to find all prime numbers from 1-1000

# empty lists for storing #s
numbers = []
# given 2 to start off the prime numbers
primes = [2]

# makes a list of every number from 2 - 1000
for i in range(2,1001):
    numbers.append(i)

# this loop is used to move through our test numbers to try all of them
for count in range(0, 100):
    # this loop moves through the individual numbers in the list individually testing them against the test number
    for w in range(0, len(numbers)):
        # if the value you are trying to index is higher or equal to the length of the list then the loop breaks and moves on to the next iteration
        if w >= len(numbers):
            break
        # if the current number is evenly dividable by the current test number and the number does not equal the test number than it is not prime
        # for example 4 is evenly dividable by 2 and does not equal 2 (4 is not prime and removed from our list of numbers)
        # 2 is dividable by 2 but is equal to 2 (2 is prime and added to the test list)
        if numbers[w] % primes[count] == 0 and numbers[w] != primes[count]:
            numbers.remove(numbers[w])
        else:
            primes.append(numbers[w])

# print the output
print("The prime numbers from 1 - 1000 are:\n",numbers)

