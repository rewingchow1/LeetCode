def maximum69Number(num):
    x = str(num)
    y = x.replace('6', '9', 1)
    return int(y)


num = 9669
out = maximum69Number(num)
print(out)
