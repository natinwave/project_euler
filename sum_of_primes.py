import math

def sum_of_primes(limit):
    # This function finds the sum of all the prime numbers below the limit.
    count = limit
    total = 2
    
    # If the input limit is even, it's stepped down to the next odd.
    if count % 2 == 0:
        count -= 1
        
    # The while loop moves the count down from the limit by the odds, and checks 
    # if they're prime numbers. If they are, the number is added to the total.
    while count > 1:
        if check_if_prime(count):
            total += count
        count -= 2
    
    return total
        
def is_divisible_5(input_num):
    # A filter to prevent unnecesary computation.
    # Returns True if the last digit of the input_num is 5 or 0 to 
    # determine if it's divisible by 5, excluding 5 itself.
    if input_num == 5:
        return False
    input_string = str(input_num)
    if input_string[len(input_string) - 1] == '5' or input_string[len(input_string) - 1] == '0':
        return True
    return False

def is_divisible_3(input_num):
    # A filter to prevent unnecesary computation.
    # Returns True if the sum of the digits of the input_num is
    # divisible by 3, exluding 3 itself.
    if input_num == 3:
        return False
    input_string = str(input_num)
    total = 0
    for char in input_string:
        total += ord(char)
    if total % 3 == 0:
        return True
    return False

def check_if_prime(input_num):
    # After a series of quick tests eliminate multiples of
    # 2, 3, and 5, a loop from 7 to sqrt(input_num) counting by odds
    # tries to divide the input_num by the counter (poss_factors) 
    # to see if it has any factors. If it has no factors, it returns True.
    
    if is_divisible_3(input_num):
        return False
    if is_divisible_5(input_num):
        return False
    if input_num == 2:
        return True
    if input_num % 2 == 0:
        return False
    poss_factors = 7
    for counter in range(2, int(math.sqrt(input_num)) / 2):
        if input_num % poss_factors == 0:
            return False
        poss_factors += 2
    return True
    
print sum_of_primes(2000000)
