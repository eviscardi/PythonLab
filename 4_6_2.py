numbers = []

for i in range(0,1000):
    isDivisible = True
    if (i%3 == 0) and (i%7 == 0):
            numbers.append(i)
            
print numbers