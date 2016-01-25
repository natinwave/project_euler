def max_consecutives_product(number_string, input_len):
    # This function, given a string of numbers, finds the consecutive segment
    # of length input_len with the greatest product of each of its digits.
    # e.g., max_consecutives_product(8124930, 2) returns 49, since 4 * 9 is greater
    # than any other 2 consecutive digits multiplied together.
    
    greatest_product = 0
    str_chunk = ""
    
    # This generates the initial chunk of numbers.
    for digit in range(0, input_len):
        str_chunk += number_string[digit]
    
    # This for loop moves the initial chunk of numbers
    # through the entire number_string.
    for digit in number_string:
        int_chunk = int(str_chunk)
        product = 1
        
        # Finds the product of the chunk digits.
        for i in range(0, input_len):
            product = product * int(str_chunk[i])
        
        # If the new product of all the chunk digits is greater 
        # than the last greatest, the greatest_product is updated.
        if product > greatest_product:
            greatest_product = product
        
        # This moves the str_chunk one more digit to the right.
        str_chunk = str_chunk[1:]
        str_chunk += digit
    
    return greatest_product


number_string = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

print max_consecutives_product(number_string, 13)
