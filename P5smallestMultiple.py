found = False
check = 0

def div1throughNum(num, top):
    sum = 0

    for i in range(1,top+1):
        if num % i == 0:
            sum = sum + 1

    if (sum == top):
        return True
    else:
        return False

while found == False:
    upBound = 20

    check = check + upBound

    if div1throughNum(check, upBound) == True:
        found = True

print(check)




