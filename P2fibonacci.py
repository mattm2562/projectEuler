nums = [1, 2]

numSum = int()
sum = 2

while numSum <= 4000000:
    if numSum % 2 == 0:
        sum = sum + numSum
    
    numSum = nums[0] + nums[1]

    nums[0] = nums[1]
    nums[1] = numSum

print(sum)
