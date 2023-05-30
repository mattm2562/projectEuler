def isPrime(num):
    import math

    prime = True
    
    for i in range (2, int(math.sqrt(num))+1):
        print(i)
        if (num % i == 0):
            prime = False

    
    return prime

print(isPrime(25))