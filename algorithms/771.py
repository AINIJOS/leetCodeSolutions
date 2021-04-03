jewels = "aA"
stones = "aAAbbbb"
count=0
for i in jewels:
    count+=stones.count(i)
print(count)
