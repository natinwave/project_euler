# This code prints the sum of every number from 0 to 1,000 which is a multiple
# of either 3 or 5.
#   x     : counter variable that increments from 0 to 1,000.
#   total : updated every time 'x' is either a multiple of 3 or 5.

x = 0
total = 0

# this for loop iterates x from 3 to 1,000.
for x in range(3, 1000):
    
    # The if/elif statement pair checks if 3 or 5 divides evenly into the 
    # current number. If either one does, it is added (only once) to the total.
    if x % 3 == 0:
        total += x
    elif x % 5 == 0:
        total += x

print total
