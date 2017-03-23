import math
import time

#Problem 3:     The prime factors of 13195 are 5, 7, 13 and 29.
#               What is the largest prime factor of the number 600851475143?


primeFactor = 1

#Determine largets Factor
def primeFactors(val):
    #loop for 2 as a factor
    while val%2==0:
        primeFactor = 2
        val = val/2
       
    #loop for odd number as factors
    f = 3
    while val!=1:
        while val % f == 0:
            primeFactor = f
            val = val/f
        f += 2
    return primeFactor

#Return Value and run time
start = time.time()

# Set for loop for multiple interations
for x in range(1): 
    a = primeFactors(600851475143)
elapsed = (time.time() - start)


#print answer
print('The largest Prime Factor is : ' + str(a) + ' Found in : ' + str(elapsed) + ' Seconds')

