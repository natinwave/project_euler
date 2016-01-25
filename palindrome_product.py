import math

def palindrome_product():
    # Finds the largest palindrome that is a multiple of two 3-digit numbers.
    # The loop starts at 999, and generates a palindrome for each iteration; 
    # first 999999, then 998899, 997799, etc. 
    
    count = 1000
    for i in range(1, 1000):
        count -= 1
        
        # Generates the palindrome by turning the count into a string,
        # reversing it, and concatenating the two strings back together.
        first_3 = str(count)
        last_3 = ""
        while len(first_3) < 3:
            first_3 = "0" + first_3
        for j in range(0, 3):
            last_3 = first_3[j] + last_3
        palindrome = int(first_3 + last_3)
        
        # This tries to find any factors of the palindrome, and makes 
        # sure they're both 3-digit numbers. The first time all 
        # requirements are met, the palindrome is returned.
        if int(math.sqrt(palindrome)) > 998:
            continue
        for poss_factors in range(2, int(math.sqrt(palindrome))):
            if palindrome % poss_factors == 0 and palindrome / poss_factors < 999:
                return palindrome

print palindrome_product()
