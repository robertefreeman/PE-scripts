# Problem #16:  Find the greatest product of five consecutive digits in the 1000-digit number.

#    

import time
import math

largeNumber = 2**1000
lSum = 0

#Create a list of digits from an integer 
def numberList(num):
 digitList = [ int(char) for char in str(num) ]
 return digitList
 
#find the sum of a list of numbers
def solution(val):
 digitList = numberList(val)
 lSum = sum(digitList) 
 return lSum


#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations (10000)
for x in xrange(1): 
   
    #Identify a specific prime    
    a = solution(largeNumber)
    
#Return run time
elapsed = (time.time() - start) 

  
#print answer
print('The sum of the digits for 2**1000 is:   %s  Found in: %s seconds') % (a,elapsed)  
 
