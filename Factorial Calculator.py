#Factorial Calculator
def factorial():
    #Take input.
    n = int(input('Enter the number whose factorial you want: '))
    
    #Check for 0
    if n == 0:
        return 1
    else:
        #Create a list for the number's range
        listn=[num for num in range(n+1)]
        listn.remove(listn[0])
       
        #Multiply through the list to get the factorial
        factorialn = 1
        for nu in listn:
            factorialn = factorialn*nu
        return (f"{n}! is {factorialn}")
