def selfDividingNumbers(left, right):
    out = []
    for i in range(left, right + 1, 1):
        count = 0
        strng = str(i)
        for element in strng:
            digit = int(element)
            if digit != 0:
                if i % digit == 0:
                    count += 1
        if count == len(strng):
            out.append(i)
    return out


left = 1
right = 22
print(selfDividingNumbers(left, right))
