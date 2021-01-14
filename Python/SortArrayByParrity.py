def sortArrayByParity(A):
    even = []
    odd = []
    for element in A:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    even.extend(odd)
    return even


Input = [3, 1, 2, 4]
print(sortArrayByParity(Input))
