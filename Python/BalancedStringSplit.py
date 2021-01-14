def balancedStringSplit(s):
    count = 0
    countl = 0
    countr = 0
    flag = True
    for i in range(0, len(s), 1):
        if (i > 0) and (s[i] != s[i - 1]):
            if flag:
                flag = False
            else:
                flag = True
        if flag:
            countl += 1
        if not flag:
            countr += 1
        if countl == countr:
            count += 1
            countl = 0
            countr = 0
    return count


s = "RLRRRLLRLL"
out = balancedStringSplit(s)
print(out)
