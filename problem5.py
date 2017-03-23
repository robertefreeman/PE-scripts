import math
import time

#Problem 5: 2520 is the smallest number that can be divided by each
#           of the numbers from 1 to 10 without any remainder.
#           
#           What is the smallest positive number that is evenly divisible
#           by all of the numbers from 1 to 20?


checklist=[11,13,14,16,17,18,19,20]

def findSmall_1():

   for x in xrange(2520,2000000000,2520):                 
       if(x%11==0 and x%13==0 and x%14==0 and x%19==0 and x%16==0 and x%17==0 and x%18==0 and x%20==0):
           return x
            

def findSmall_2():
    
    for x in xrange(2520,2000000000,2520):
        if all(x%lis==0 for lis in checklist):
            return x

       

#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations
for x in range(1): 
    a1 = findSmall_1()

#Return run time
elapsed1 = (time.time() - start)


#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations
for x in range(1): 
    a2 = findSmall_2()

#Return run time
elapsed2 = (time.time() - start)


#print answer
print('Smallest number evenly divisible by range(1:20): %s Found in: %s seconds') % (a1,elapsed1)

print('Smallest number evenly divisible by range(1:20): %s Found in: %s seconds') % (a2,elapsed2) 



