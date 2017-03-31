# Problem #20 :     n! means n * (n - 1) * ... * 3 * 2 * 1

#                   For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
#                   and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#                   Find the sum of the digits in the number 100!

#Solved 648

import time
import math


def digitSum(num):
    numProd = num
    numSum = 0
    # Find product of numbers in num!
    for x in range(num-1,0,-1):
        numProd *= x

    #find sum of digits in list
    for n in str(numProd):
        numSum += int(n)

    return numSum

# Start run time clock for function 1
start = time.time()

# Set for loop for multiple interations (10000)
for x in xrange(1):

    # Find sum of a number!
    a = digitSum(100)

# Return run time
elapsed = (time.time() - start)

# print answer
print('The sum of the Digits in 100! is: %s. Solution found in: %s seconds') % (a, elapsed)