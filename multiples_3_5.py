# This code prints the sum of every number from 0 to 1,000 which is a multiple
# of either 3 or 5.
#   x     : counter variable that increments from 0 to 1,000.
#   total : updated every time 'x' is either a multiple of 3 or 5.

total = 0
divisible_3_or_5 = [i for i in range(3, 1000) if i % 3 == 0 or i % 5 == 0 ]

# this for loop iterates x through all the numbers that are divisible by either
# 3 or 5, and adds them to the total.
for x in divisible_3_or_5:
    total += x

print total
