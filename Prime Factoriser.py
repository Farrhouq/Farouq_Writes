#A function that returns the prime factorization of a given number.
def prime_factorisation():
    
    #A sub-function that checks for prime numbers.
    def prime(n):
        prist=[]
        for num in range(1, n+1):
            if n%num==0:
                prist.append(num)
        return len(prist) == 2
    
    #Another subfunction that does the factorisation.
    def factorisation(fac_list, number):
        left = number
        count = 0
        l=[]
    
        for n in fac_list:
            listed = []

            count = 0
            while left%n == 0:
                if left%n == 0:
                    left = left/n
                    count += 1
                    if left%n != 0:
                        listed.append(count)
                        if count != 1:
                            l.append('('+str(n)+'^'+str(count)+')')
                        else:
                            l.append(str(n))
                    
        return ' x '.join(l)            
    
    #Take input from user.
    
    root = int(input("Enter a number and I will return the prime factorisation of that number: "))
    factors=[]
    
    #Creating a list of factors of the number.
    for n in range(1,root+1):
          if root%n == 0:
                factors.append(n)
    
    #Sieving out prime factors from the factors list.
    prime_factors=[]            
    for factor in factors:
        if prime(factor):
            prime_factors.append(factor)
            
    #Return the prime factorization. 
    print(f'The prime factorisation of {root} is ({factorisation(prime_factors, root)})')
