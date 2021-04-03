items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"
newItems=[]
count = 0
for i in items:
    if ruleKey == "type":
        newItems.append(i[0])
    elif ruleKey == "color":
        newItems.append(i[1])
    elif ruleKey == "name":
        newItems.append(i[2])
for j in newItems:
    if j==ruleValue:
        count+=1
print(count)
