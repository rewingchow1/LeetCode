def repeatedNTimes(A):
    for i in range(len(A)):
        count = 0
        for j in range(len(A)):
            if A[i] == A[j]:
                count += 1
            if count > 1:
                return A[i]


input = [5, 1, 5, 2, 5, 3, 5, 4]
print(repeatedNTimes(input))
