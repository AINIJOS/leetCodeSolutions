n = 234
n = str(n)
newList = []
product = 1
sum = 0
for i in range(len(n)):
    product *= int(n[i])
    sum += int(n[i])
print(product-sum)