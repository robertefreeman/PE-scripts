# Problem 19:   You are given the following information, but you may prefer to do some research for yourself.
#               
#               1 Jan 1900 was a Monday.
#               Thirty days has September,
#               April, June and November.
#               All the rest have thirty-one,
#               Saving February alone,
#               Which has twenty-eight, rain or shine.
#               And on leap years, twenty-nine.
#
#               A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#               How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#Solved 171

import time
import math

monthTbl = {  1:0,
            2:3,
            3:3,
            4:6,
            5:1,
            6:4,
            7:6,
            8:2,
            9:5,
            10:0,
            11:3,
            12:5,
        }
yearCode = lambda x: (x + (x / 4)) % 7

def isSunday():
    x = 0
    for year in range(1,101):
        for mon in range(1,13):
            # Add Century code
            if year <100:
                val = 0
            else:
                val = 6
            #Add year code
            val += yearCode(year)
            #Add Month code
            val += monthTbl[mon]
            #Add day number
            val += 1
            #determine if sunday
            if isLeap(year) == True:
                if mon == 1 or mon == 2:
                    val -= 1
            if val % 7 == 0 :
                x += 1
    return x

def isLeap(year):
    if year % 4 == 0:
        return True
    else:
        return False

#Start run time clock for function 1 
start = time.time()

# Set for loop for multiple interations (10000)
for x in xrange(1): 
   
    #Identify a specific prime    
    a = isSunday()   
#    a = solution(largeNumber)
    
#Return run time
elapsed = (time.time() - start) 

  
#print answer
print('%s Sundays fell on the first of the month during the 20th century. Solution found in: %s seconds') % (a,elapsed)  