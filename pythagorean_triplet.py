import math

def pythagorean_triplet(limit):
    # If a, b, and c are a Pythagorean triplet, then this function returns a*b*c if a+b+c = limit.
    # The two equations: 
    #      a^2 + b^2 = c^2 
    #
    # and 
    #      a + b + c = limit 
    # 
    # can be used to determine b as a function of a (with limit as a constant):
    #      b(a) = (limit ** 2 - 2 * limit * a) / (2 * limit - 2 * a)

    for a in range(1, int(limit / (2 + math.sqrt(2)))):
        
        # A for loop is used to test values of a, thus generating a value of b.
        b = (limit ** 2 - 2 * limit * a) / (2 * limit - 2 * a)
        
        # The pythagorean thereom is then used to find c. 
        c = math.sqrt(a**2 + b**2)
        
        # Checks if c is a whole number.
        if c % 1 == 0:
            # If it is, then a, b, and c form a pythagorean triplet, and 
            # their product is returned.
            return a * b * c
            
print pythagorean_triplet(1000)
