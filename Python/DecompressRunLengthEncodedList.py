def decompressRLElist(nums):
    out = []
    for i in range(0, int(len(nums) / 2), 1):
        a = nums[2 * i]
        b = nums[2 * i + 1]
        for j in range(0, a, 1):
            out.append(b)
    return out


nums = [1, 2, 3, 4]
encodelist = decompressRLElist(nums)
print(encodelist)
