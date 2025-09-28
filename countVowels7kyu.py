#Title of the kata
    #Vowel Count

#Link to the kata on Codewars:
    #https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

#Your solution code:
    #As seen below.

#A short explanation (3–4 sentences) of how your solution works.
    #It loops through the string checking for vowels, adding one to the counter as it goes. 

#---------------------------------------------------------------------------------------------

def get_count(sentence):
    
    #create a counter to store the number of vowels
    count = 0
    
    #loop through the string and return number of vowels
    for character in sentence :

        #check if the string contains aeiou
        if (character in "aeiou") :
            #add one to the count for every vowel found
            count += 1
        
    
    return count

        
    
