def even_fibonacci(upper_limit):
    # This code prints the sum of all even fibonacci numbers, counting up to upper_limit. 
    #   x      : the current number in the fibonacci sequence.
    #   x_last : the prior number. 
    #   total  : updated every time a new even number in the sequence is found.
    
    x = 1
    x_last = 0
    total = 0
    
    # this loop iterates until x matches the upper limit. 
    while x < upper_limit:
        
        # the first three lines increment x and x_last.
        temp = x
        x += x_last
        x_last = temp
        
        # the if statement will add the current number 'x' to the total if it's even.
        if x % 2 == 0:
            total += x
            
    return total
    
print even_fibonacci(4000000)
