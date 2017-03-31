# Problem 17:   If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
#               $3+3+5+4+4=19$ letters used in total. If all the numbers from 1 to 1000 (one thousand) inclusive were 
#               written out in words, how many letters would be used?

#Solved: 21124

import time
import math

singles = [0,3,3,5,4,4,3,5,5,4]
teens = [3,6,6,8,8,7,7,9,8,8]
tens = [6,6,5,5,5,7,6,6]
hundreds = 7
thousand = 11
And = 3


def solution():
    #Count letters from 1 - 19
    total = sum(singles) + sum(teens)
    #Count letters from 20 - 99
    for x in tens:
        for y in singles:
            total += x + y
    #Count letters from 100 - 999
    print total
    for h in singles[1:]:
        hunStep = h + hundreds + And
        #numbers 100 - 109 etc ...
        for s in singles:
            if s == 0:
                total -= 3
            total += hunStep + s
        #numbers 110 -119 etc ...
        for t in teens:
            total += hunStep + t
        #numbers 120 - 199 etc ...
        for t2 in tens:
            for y in singles:
                total += hunStep + t2 + y
            
    total+= thousand
    return total
    
    


#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations (10000)
for x in xrange(1): 
   
    #Identify a specific prime    
    a = solution()
    
#Return run time
elapsed = (time.time() - start) 

  
#print answer
print('%s letters were used counting from 1 - 1000: Found in: %s seconds') % (a,elapsed)  