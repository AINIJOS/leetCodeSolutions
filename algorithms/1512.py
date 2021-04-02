nums = [1, 2, 3, 1, 1, 3]
count = 0
for i in range(0, len(nums)):
    for j in range(1, len(nums)):
        if nums[i] == nums[j] and i < j:
            count += 1
print(count)
