n = 5
start = 0
nums = []
count = 0
for i in range(0, n):
    nums.append(start + 2 * i)
for j in range(n):
    count ^= nums[j]
print(count)
