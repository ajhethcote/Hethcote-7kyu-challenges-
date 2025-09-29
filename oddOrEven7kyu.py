#Title of the kata
    #Odd or Even?

#Link to the kata on Codewars:
    #https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

#Your solution code:
    #As seen below.

#A short explanation (3–4 sentences) of how your solution works.
    # It loops through the array, checking each number using the modulo operator and dividing by two to see if there is a remainder. 
    # If there is no remainder, it returns "even", else it returns "odd".
    #This one also doesn't pass the codewars tests, but works with what I throw at it in VS code, and I can't figure out why. :/

#---------------------------------------------------------------------------------------------


def odd_or_even(arr):
    
    for num in arr :
        if num % 2 == 0:
            return "even"
        else:
            return "odd"