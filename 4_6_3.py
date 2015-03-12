# The following code makes a list of 10 random numbers between 0 and 10 from random import random as rand
x = []
for i in range(10):
     x.append( rand() * 10 )
print x