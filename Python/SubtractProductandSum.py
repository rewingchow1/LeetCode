def subtractProductAndSum(n):
    x = str(n)
    lst = []
    product = 1
    sum = 0
    for i in x:
        lst.append(int(i))
    for j in lst:
        product = product * j
    for k in lst:
        sum = sum + k
    out = product - sum
    return out


n = 234
out = subtractProductAndSum(n)
print(out)
