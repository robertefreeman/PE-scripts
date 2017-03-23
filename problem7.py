import math
import time

#Problem 7:     By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#               we can see that the 6th prime is 13. What is the 10,001st prime number?


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

def findPrime(val):
    primeCount = 0
    finalPrime = 0
    x = 1
    while primeCount <= val:
        if isPrime(x):
            primeCount += 1
            finalPrime=x
            if primeCount==val:
                return finalPrime
        x+=1

#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations (10000)
for x in range(1): 
   
    #Identify a specific prime    
    a = findPrime(10001)
    
#Return run time
elapsed = (time.time() - start)


#print answer
print('The 10001st Prime is :   %s  Found in: %s seconds') % (a,elapsed)
  




