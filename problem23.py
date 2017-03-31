# Problem #23 :     A perfect number is a number for which the sum of its proper divisors is exactly equal to the
#                   number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
#                   which means that 28 is a perfect number.

#                   A number n is called deficient if the sum of its proper divisors is less than n and it is called
#                   abundant if this sum exceeds n.

#                   As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
#                   written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
#                   all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
#                   upper limit cannot be reduced any further by analysis even though it is known that the greatest
#                   number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#                   Find the sum of all the positive integers which cannot be written as the sum of two abundant
#                   numbers.

#

import time
import math

# Find all sum of all proper divisors
def sumOfDiv(num):
    sumDiv = 0
    for x in xrange(1, int(math.sqrt(num))):
        if num % x == 0:
            sumDiv += num/x
            sumDiv += x
    return sumDiv-num


# Find amicable pairs up to variable: num
def propDivList(num):
    divList = []
    sumDiv = 0
    for x in xrange(num):
        divList.append([x,sumOfDiv(x)])

    for f in range(len(divList)):
        for l in range(len(divList)):
            if divList[f][0] == divList[l][1] and divList[f][1] == divList[l][0] and divList[f][0] != divList[l][0]:
                print(str(divList[f][0]) + ':' + str(divList[l][1]) + '   ') + str(divList[f][0]) + ':' + str(divList[l][0])
                sumDiv += divList[f][0] + divList[l][0]

    return sumDiv/2




# Start run time clock for function 1
start = time.time()

# Set for loop for multiple interations (10000)
for x in xrange(1):
    # Identify a specific prime
    a = propDivList(10000)
# a = solution(largeNumber)

# Return run time
elapsed = (time.time() - start)

# print answer
print('The sum of all amicable pairs under 10000 is: %s . Solution found in: %s seconds') % (a, elapsed)