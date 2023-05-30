
def palCheck(num):
    pal = str(num)
    palLen = int(len(pal))
    check = True

    for i in range(0, int(palLen / 2)):
        if pal[i] != pal[(palLen - i - 1)]:
            check = False
    
    return check
max = 0

for i in range(100,1000):
    for j in range(100,1000):
        prod = i * j

        if palCheck(prod):
            if prod > max:
                max = prod

print(max)