# Problem #21 :     Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
#                   into n). If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a
#                   and b are called amicable numbers.

#                   For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
#                   d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#                   Evaluate the sum of all the amicable numbers under 10000.

#Solved 31626

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