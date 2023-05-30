def isPrime(num):
    import math

    prime = True
    
    for i in range (2, int(math.sqrt(num))+1):
        if (num % i == 0):
            prime = False

    
    return prime

primeList = list()
primeCount = 2
order = 10001
num = 3
prime = 0

while primeCount < order:
    num += 2
    
    if isPrime(num):
        print(str(primeCount + 1) + ", " + str(num))
        primeCount = primeCount + 1
    
print(num)