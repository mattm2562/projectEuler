num = 600851475143

for i in range(1, num):
    if (num % i == 0) and i > 2:
        prime = True

        for j in range (2, i):
            if (i % j == 0):
                prime = False
        
        if prime == True:
            print(i)
