# arr = [7, 1, 14, 11]
# val = False
# for i in range(0, len(arr)):
#     for j in range(len(arr)):
#         if arr[i] / 2 == arr[j]:
#             val = True
#             break
# print(val)

arr = [7, 1, 14, 11]
val = False
for i in range(len(arr)):
    for j in (arr[:i] + arr[i + 1:]):
        if 2*arr[i] == j:
            val = True
            break
print(val)
