import math
import time

#Problem 10:  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.


#check if number is prime
def isPrime(num):
    
    # We know 1 is not a prime number
    if num == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= num:
        # Check if i divides x without leaving a remainder
        if num % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


#Find Specific Primes
def findPrimeSum(val):
    primeSum = 2
    x = 3
    while x <= val:
        if isPrime(x):
            primeSum += x
        x+=2
    return primeSum
    
#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations (10000)
for x in range(1): 
   
    #Identify a specific prime    
    underCount = 2000000
    a = findPrimeSum(underCount)
    
#Return run time
elapsed = (time.time() - start)


#print answer
print('The sum of Primes under %s =  %s  Found in: %s seconds') % (underCount,a,elapsed)



