sumSquares = 0
sum = 0

for i in range(1,101):
    sumSquares = sumSquares + (i ** 2)
    sum = sum + i

print((sum**2) - sumSquares)