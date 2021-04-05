command = "G()()()()(al)"
# newstr = command.replace('()', 'o').replace('(al)', 'al')
# print(newstr)

###### without replace() ######

#1)
###### with dict ######
newDict = {
    "()": "o",
    "(al)": "al",
    "G": "G"
}

a = ''
b = ''

for i in range(len(command)):
    a += command[i]
    if a in newDict:
        b += newDict[a]
        a=""
print(b)

#2)
###### with slices ######

# b = ''
# for i in range(len(command)):
#     if command[i] == 'G':
#         b+='G'
#     elif command[i] == '(' and command[i + 1] == ')':
#         b += 'o'
#     elif command[i] == '(' and command[i + 3] == ')':
#         b +='al'
# print(b)



################################################################################################

###### garbage ######

# for i in command:
#     sukableat = command.index(i)
#     if i == '(' and command[sukableat + 1] == ')':
#         command = command[:command.find(i)] + 'o' + command[(command.find(i) + 2):]
#
# print(command)

# newstr=''

# for i in range(0, len(command)):
#     if command[i] == '(':
#         newstr = command[:i] + 'o' + command[i+2:]
#         command=newstr
#
# print(command)
