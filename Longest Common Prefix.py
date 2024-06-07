# Input: strs = ["flower","flow","flight"]
# Output: "fl"

srts = input().split()
prefix = ""
menor = min(srts)
flag = True

for i in range(len(menor)): # 4
    for word in srts:
        if word[i] != menor[i]:
            flag = False
            break
    if flag == False:
        break
    else:
        prefix += menor[i]
print(prefix)
