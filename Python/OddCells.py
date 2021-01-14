def oddCells(n, m, indices):
    mtrx = []
    odd = 0
    for i in range(0, n, 1):
        rows = []
        for j in range(0, m, 1):
            rows.append(0)
        mtrx.append(rows)
    for incr in indices:
        for k in range(0, len(incr), 1):
            if k == 0:
                rowincr = incr[k]
                for l in range(0, m, 1):
                    mtrx[rowincr][l] += 1
            if k == 1:
                colincr = incr[k]
                for element in mtrx:
                    element[colincr] += 1
    for x in range(n):
        for y in range(m):
            if mtrx[x][y] % 2 != 0:
                odd += 1
    return odd


n = 2
m = 3
indices = [[0, 1], [1, 1]]
out = oddCells(n, m, indices)
print(out)
