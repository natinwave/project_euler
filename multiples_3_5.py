x = 0
total = 0
for x in range(3, 1000):
    if x % 3 == 0:
        total += x
    elif x % 5 == 0:
        total += x
print total
