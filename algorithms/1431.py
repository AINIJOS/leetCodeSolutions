candies = [2,3,5,1,3]
extraCandies = 3

maxCandies = max(candies)
for i in range(0, len(candies)):
    if candies[i] + extraCandies >= maxCandies:
        candies[i] = True
    else:
        candies[i] = False
print(candies)

