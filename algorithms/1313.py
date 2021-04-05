nums = [1,1,2,3]
newNums1=[]
for i in range(0,len(nums),2):
    for j in range(0,nums[i]):
        newNums1.append(nums[i+1])
print(newNums1)
