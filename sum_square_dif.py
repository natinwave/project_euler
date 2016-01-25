def sum_square_dif(input_num):
    
    # This function finds the sum_of_squares of all the integers 
    # from 1 to the input_num (i.e. 1^2 + 2^2 + 3^2 = 14).
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, input_num + 1):
        sum_of_squares += i ** 2
        
    # It then finds the square_of_sum of all the integers from 
    # 1 to the input_num (i.e. (1 + 2 + 3)^2 = 36).
    for i in range(1, input_num + 1):
        square_of_sum += i
    square_of_sum = square_of_sum ** 2
    
    # It then returns the difference of the two.
    return square_of_sum - sum_of_squares

print sum_square_dif(100)
