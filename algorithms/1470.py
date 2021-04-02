nums = [2, 5, 1, 3, 4, 7]
n = 3
count = 1
for i in range(n, len(nums)):
    nums.insert(count, nums[i])
    count += 2
    nums.pop(i+1)
print(nums)
