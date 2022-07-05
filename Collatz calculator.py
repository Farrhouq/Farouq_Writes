#Computes the time of flight of an integer in the Collatz Conjencture.
def collatz_time_of_flight():
    n = int(input("Enter a number: "))
    n2 = n
#Declare the time of flight variable.
    step = 0

#The while loop to proceed with the Collatz's rules.
    while n != 1:
        if n % 2 == 0:
            n = n/2
            step += 1
        else: 
            n = 3*n + 1
            step += 1
            
#The final answer.
    return f"The time of flight for {n2} is {step}s"
        
