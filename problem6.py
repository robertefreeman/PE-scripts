import math
import time

#Problem 6:     The sum of the squares of the first ten natural numbers is,

#               (1+2+\cdots+10)^2=55^2=3025.
#           
#               Hence the difference between the sum of the squares of the first ten natural numbers and 
#               the square of the sum is:

#               3025-385=2640. 
    
#               Find the difference between the sum of the squares of the first one hundred natural 
#               numbers and the square of the sum.


sumofsquares = 0
squareofsums = 0

#Find the sum of all squares     
def sumSquares(count):

    sos = 0
    for x in range(1,count+1):
        sos += x**2 
    return sos       
    


#Find the square of all sums method #1          ---- Slower ----       
def squareSums1(count):
    
    sos = 0
    for x in range(1,count+1):
        sos += x 
    return sos**2    
       
#Find the square of all sums method #2          ---- FASTER ----
def squareSums2(count):

    tot = ((count+1)*count)/2
    sos = tot**2
    return sos 

#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations (10000)
for x in range(10000): 
   
    #Find difference using method 2    
    a = squareSums2(100) - sumSquares(100)
    
#Return run time
elapsed = (time.time() - start)


#print answer
print('Sum of squares for 10:   %s  Found in: %s seconds') % (a,elapsed)
  




