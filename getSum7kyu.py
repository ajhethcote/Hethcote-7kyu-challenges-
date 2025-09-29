#Title of the kata
    #Beginner Series #3 Sum of Numbers

#Link to the kata on Codewars:
    #https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

#Your solution code:
    #As seen below.

#A short explanation (3–4 sentences) of how your solution works.
    #if an and b are not equal, loop through the range between a and b to find the sum.
    #if an and b are equal, return a. 
    #This one doesn't work all the way, and I'm not sure why. :/
#---------------------------------------------------------------------------------------------

def get_sum(a,b):
    
    #create a counter for the loop 
    count = 0
    
    #if an and b are not equal, loop through the range between a and b to find the sum. 
    if a != b :
        for n in range(a , b) :
            count += 1
        return count
    
    #if an and b are equal, return a. 
    elif a == b :
        return a
    
