def isPrime(num):
    import math

    prime = True
    
    for i in range (2, int(math.sqrt(num))+1):
        if (num % i == 0):
            prime = False
  
    return prime


sum = 2
uBound = 2000000
num = 3

while num < uBound:
    if isPrime(num):
        sum = sum + num

        print(num)
    
    num += 2

print(sum)

