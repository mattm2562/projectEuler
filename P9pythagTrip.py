import math

for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a**2 + b**2)

        if c % 1 == 0 and a < b and (a+b+c) == 1000:
            print (str(a) + ", " + str(b) + ", " + str(math.sqrt(a**2 + b**2)))
            print (a*b*c)

