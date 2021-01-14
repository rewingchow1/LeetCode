def twoSum(nums, target):
    for i in range(0, len(nums), 1):
        sum = None
        if nums[i] < target:
            for j in range(0, len(nums), 1):
                if nums[j] < target:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        break
        if sum == target:
            break
    return [i, j]


nums = [11, 25, 4, 5]
target = 9
x = twoSum(nums, target)
print(x)
