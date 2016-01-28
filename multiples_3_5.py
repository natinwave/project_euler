def multiples_3_5(upper_limit):
    # Finds the sum of every number from 0 to an upper_limit 
    # which is a multiple of either 3 or 5.
    
    # This creates a list of all the numbers from 0 to the 
    # upper_limit that are divisible by 3 or 5.
    divisible_3_or_5 = [i for i in range(3, upper_limit) if i % 3 == 0 or i % 5 == 0 ]
    
    # Returns the sum of all the elements in divisible_3_or_5.
    return sum(divisible_3_or_5)

print multiples_3_5(1000)
