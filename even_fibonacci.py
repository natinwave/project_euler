# This code prints the sum of all even fibonacci numbers, counting up to 4 million. 
#   x      : the current number in the fibonacci sequence.
#   x_last : the prior number. 
#   total  : updated every time a new even number in the sequence is found.

x = 1
x_last = 0
total = 0

# this for loop iterates through the first 33 fibonacci numbers, which cuts it off at 4 million. 
# a is just a counter variable and isn't used.
for a in range(0, 32):
    
    # the first three lines increment x and x_last.
    temp = x
    x += x_last
    x_last = temp
    
    # the if statement will add the current number 'x' to the total if it's even.
    if x % 2 == 0:
        total += x
        
print total
    
