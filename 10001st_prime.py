import math

def prime_number(input_num):
    # Uses check_if_prime to determine when the count is prime, which 
    # jumps by 2 to only cover the odd numbers. When the count is prime,
    # the total increases by one. Once the total number of primes counted
    # matches the input_num, the count (the most recent prime) is returned.
    total = 0
    count = -1
    # If the user asks for the first prime, 2 is returned since it's an exception.
    if input_num == 1:
        return 2
    while total < input_num:
        count += 2
        if check_if_prime(count):
            total += 1
    return count

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

print prime_number(10001)
