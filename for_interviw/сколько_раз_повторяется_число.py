lis = [1, 1, 3, 2, 1, 3, 4]
dic={}
for i in range(len(lis)):
    k = 1
    for l in range(i+1,len(lis)):
        if lis[l]==lis[i]:
            k += 1
    if lis[i] not in dic:
        dic.update({lis[i]:k})
print(dic)