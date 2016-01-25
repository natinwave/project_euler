def smallest_multiple(upper_limit):
    
    # This function finds the smallest number which can be
    # evenly divided by each number from 1 up to the upper_limit.
    # It is recursive in nature, using the fact that the smallest
    # multiple of all the numbers from 5 down, for example, is simply
    # going to be some multiple of the smallest common multiple from 4 down.
    
    count = 0
    while True:
        count += 1
        if upper_limit == 1:
            return 1

        # The result from the nested function is multiplied by the count
        # until the product is evenly divisible by the upper_limit.
        # The product is returned.
        possible_ans = smallest_multiple(upper_limit - 1) * count
        if possible_ans % upper_limit == 0:
            return possible_ans

print smallest_multiple(20)
