
# Problem #8:  A Pythagorean triplet is a set of three natural numbers,  such that

#For example 3^2 + 4^2 = 5^2, . There exists exactly one Pythagorean triplet for which a + b + c = 1000 . Find the product .

import time

# Determine trip value
tripVal = lambda m, n: (n**2 - m**2) + (2*n*m) + (n**2 + m**2)
aVal = lambda m, n: n**2 - m**2
bVal = lambda m, n: 2*n*m
cVal = lambda m, n: n**2 + m**2

#find the solution to Problem #9 
def solution():
 for x in xrange(1,200):
  for y in xrange(x+1,100):
   val = tripVal(x,y)
   if val == 1000:
    a = aVal(x,y)
    b = bVal(x,y)
    c = cVal(x,y)
    return (a*b*c)



#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations (10000)
for x in xrange(1): 
   
    #Identify a specific prime    
    a = solution()
    
#Return run time
elapsed = (time.time() - start) 

  
#print answer
print('The sum of the Pythagorean triplet with a sum of (a, b, c) values = 1000 is:   %s  Found in: %s seconds') % (a,elapsed)  
 
