nums = [8,1,2,2,3]
ans=[]
for i in range(0, len(nums)):
    count = 0
    for j in range(0, len(nums)):
        if j != i and nums[i] > nums[j]:
            count += 1
    ans.append(count)
print(ans)


