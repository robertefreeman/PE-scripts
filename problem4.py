import math
import time

#Problem 4:   A palindormic number reads the same both ways. 
#           The largest palindrome made from the product of two 2-digit numbers is 9009, which is 91 times 99 . 
#           Find the largest palindrome made from the product of two 3-digit numbers.




#Determine if number is palindormic
def isPal(num):
    rev = str(num)[::-1]
    if rev==str(num):
        return True
        

#Find largest product of 2, 3 digit numbrs that is palindormic        
def findLarge():
    larPal = 1
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            if isPal(x*y):
                larPal=x*y
                return larPal
                #if x*y > larPal :
                #    larPal = x*y
    #return larPal
       

#Start run time clock
start = time.time()

# Set for loop for multiple interations
for x in range(1): 
    a = findLarge()

#Return run time
elapsed = (time.time() - start)


#print answer
print('Largest palindormic number from the product of 3 digits numbers: %s in: %s seconds') % (a,elapsed)   



