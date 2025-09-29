#Title of the kata
    #Highest and Lowest

#Link to the kata on Codewars:
    #https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

#Your solution code:
    #As seen below.

#A short explanation (3–4 sentences) of how your solution works.
    #Converts the string into a list so that we can use min() and max(), than converts the result of the methods back into strings and returns the 
    # answer in the specified format. 

#---------------------------------------------------------------------------------------------

def high_and_low(numbers):
 
    #split the string into a list so we can use list functions on it
    numList = numbers.split(" ")

    #get min and max and convert back into str data
    high = str(max(numList))
    low = str(min(numList))
    
    #return min and max as a string of two numbers with a space between them. 
    return (f"{high} {low}")

