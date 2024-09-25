import numpy as np
import time
import math


# semi standard way of calculating if a number is prime or not
def PrimeNumbers(i):
    for x in range(2, i//2): # uses all numbers up to half of the given int in order to decrease the total amount of numbers measured in order to tell if a number is prime or not
        if i%x == 0:
           return
    print(i)

# uses every number up to the square root of the given int to calculate if its prime
def PrimeNumbersSqrt(i):
    for x in range(2, math.ceil(math.sqrt(i))+1):
        if i%x == 0:
           return
    print(i)

# counts the amount of prime numbers in the indicated range
def PrimeNumbersSqrtCounter(i):
    for x in range(2, math.ceil(math.sqrt(i))+1):
        if i%x == 0:
           return
    global cont
    cont += 1
    print(cont)


# creates a list of prime numbers and compares each number to the already existing prime numbers.
def PrimeNumbersList(i):
    global primeArray
    for prime in primeArray:
        if i%prime == 0:
            return
    primeArray.append(i)



cont = 1 # is used as a counter to count the total amount of prime numbers
i = 2 # variable needs to be changed to 2 in order to correctly get the result in the PrimeNumbersList function
primeArray = [2]
start_time=time.time()
while (i < 100): # determines the amount of prime numbers that will be calculated
    PrimeNumbersList(i)
    i += 1 # must also be modified to 1 in order for the PrimeNumbersList function to work correctly
end_time=time.time()
print(primeArray)
print(end_time-start_time)
