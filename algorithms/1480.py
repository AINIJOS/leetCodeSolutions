nums = [1,2,3,4]
tmp = 0
for i in range(0, len(nums)):
    tmp += nums[i]
    nums[i] = tmp
print(nums)

