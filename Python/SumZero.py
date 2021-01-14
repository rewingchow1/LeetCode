def sumZero(n):
    out = []
    if n % 2 == 0:
        for i in range(1, int(n/2)+1, 1):
            out.append(i)
            out.append(i * -1)
    else:
        out.append(0)
        n = n - 1
        for i in range(1, int(n/2)+1, 1):
            out.append(i)
            out.append(i * -1)
    out.sort()
    return out


n = 5
print(sumZero(n))
