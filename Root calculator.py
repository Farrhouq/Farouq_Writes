#Checks the exponent of one number needed to get another.

def power(num, factor) :
    times = 0
    conti = True
    while num != 1:
        while conti:
            if num == 1:
                break
            num = num/factor
            times += 1
    return times
