def numJewelsInStones(J, S):
    count = 0
    for jewels in J:
        for stones in S:
            if jewels == stones:
                count += 1
    return count


J = "z"
S = "ZZ"
out = numJewelsInStones(J, S)
print(out)
