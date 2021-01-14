def flipAndInvertImage(A):
    out = []
    for row in A:
        row.reverse()
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = 1
            else:
                row[i] = 0
    return A


Input = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(flipAndInvertImage(Input))