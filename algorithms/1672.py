# accounts = [[1, 2, 3], [3, 2, 1]]
#
# asd = max(accounts) ???
# print(sum(asd))

accounts = [[2,8,7],[7,1,3],[1,9,5]]
asd=[]

for i in range(0, len(accounts)):
    asd.append(sum(accounts[i]))

print(max(asd))
