def findNumbers(nums):
    count = 0
    for x in nums:
        number = str(x)
        if len(number) % 2 == 0:
            count += 1
    return count


nums = [555, 901, 482, 1771]
out = findNumbers(nums)
print(out)
