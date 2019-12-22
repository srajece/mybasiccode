def max_factor(num):
    """Find the maximum prime factor."""
    factor = 2
    while factor * factor <= num:
        while num % factor == 0:
            num /= factor
        factor += 1
    if (num > 1):
        return num
    return factor

print (max_factor(33)) 
print (max_factor(38)) 
print (max_factor(600851475143)) 
