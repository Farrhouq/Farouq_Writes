#Fibonacci Generator
def generate_fibonacci():
    #Take a number as input.
    number = input('Enter a number: ')
    
    #Define the iterating variable.
    i = 1
    
    #The Fibonacci list
    liste= [0,1]
        
    #Summing the last two numbers in the Fibonacci list and adding this sum to the list.   
    while i < int(number):
        current_sum = liste[-1] + liste[-2]
        liste.append(current_sum)
        i += 1
    #Return the Fibonacci list ommitting the beginning '0'.
    liste.remove(liste[0])   
    return liste      
