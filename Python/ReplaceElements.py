def replaceElements(arr):
    out = []
    for i in range(len(arr)):
        temp = []
        temp.extend(arr[i + 1::])
        temp.sort()
        if temp:
            out.append(temp[len(temp) - 1])
        else:
            out.append(-1)
    return out


arr = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr))
