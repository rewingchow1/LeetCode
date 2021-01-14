def numberOfSteps(num):
    count = 0
    flag = True
    while flag:
        count += 1
        check = num % 2
        if check == 0:
            num = num/2
        if check == 1:
            num -= 1
        if num == 0:
            flag = False
    return count


num = 8
out = numberOfSteps(num)
print(out)
