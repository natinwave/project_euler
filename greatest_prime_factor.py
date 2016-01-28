import math
# biggest_prime_factor receives a number, and finds its greatest prime factor.
# The algorithm has a complexity of log(n).

def biggest_prime_factor(input_num):
    
    # This loop starts from 2 and counts to the sqrt(input_num),
    # checks if the input_num is divisible by the count,
    # and then checks if that dividend is a prime number. 
    # The first prime dividend it finds will be the greatest prime factor.
    count_prime = 0
    for count in range(2, int(math.sqrt(input_num))):
        
        # checks if the count divides evenly into the input_num.
        if input_num % count == 0:
            
            # count_prime keeps a record of the greatest prime counter;
            # e.g., for input = 50, the loop will count from 2 to 7.
            # It'll get to 7 and stop, not finding any prime dividends. However, 
            # count_prime will know that it counted past 5, which is a prime number.
            # 5 is then returned as the greatest prime factor at the end.
            if check_if_prime(count):
                count_prime = count
                
            # possible_prime is the dividend that needs to be checked 
            # to see if it's prime. If it is prime, it's returned.
            possible_prime = input_num / count
            if check_if_prime(possible_prime):
                return possible_prime
                
    # If it reaches the end of the loop and count_prime was never set,
    # the input_num must be prime and is itself returned.
    if count_prime == 0:
        return input_num
        
    # Otherwise, the largest count_prime is returned.
    else:
        return count_prime

def is_divisible_5(input_num):
    # A simple filter to prevent unnecesary computation.
    # checks if the last digit of the input_num is 5 to 
    # determine if it's divisible by 5, excluding 5 itself.
    if input_num == 5:
        return False
    input_string = str(input_num)
    if input_string[-1] == '5' or input_string[-1] == '0':
        return True
    return False

def is_divisible_3(input_num):
    # A simple filter to prevent unnecesary computation.
    # checks if the last digit of the input_num is 3 to 
    # determine if it's divisible by 3, excluding 3 itself.
    if input_num == 3:
        return False
    input_string = str(input_num)
    total = 0
    for char in input_string:
        total += ord(char)
    if total % 3 == 0:
        return True
    return False

def is_even(input_num):
    # This is a way to test if a number is even, without using the more 
    # expensive modulo function. 
    # It checks if the last digit is even to determine if the whole 
    # number is as well.
    input_str = str(input_num)
    if int(input_str[-1]) % 2 == 0:
        return True
    return False

def check_if_prime(input_num):
    # After a series of quick tests eliminate multiples of
    # 2, 3, and 5, a loop from 7 to sqrt(input_num) counting by odds
    # tries to divide the input_num by the counter (poss_factors) 
    # to see if it has any factors.
    
    if is_divisible_3(input_num):
        return False
    if is_divisible_5(input_num):
        return False
    if input_num == 2:
        return True
    if is_even(input_num):
        return False
    poss_factors = 7
    for counter in range(2, int(math.sqrt(input_num)) / 2):
        if input_num % poss_factors == 0:
            return False
        poss_factors += 2
    return True

print biggest_prime_factor(600851475143)
