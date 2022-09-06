Clist = list(map(int, input().split()))

cList = [1, 1, 2, 2, 2, 8]

oList = []
for i in range(6):
    if Clist[i] != cList[i]:
        oList.append(cList[i] - Clist[i])
    elif Clist[i] == cList[i]:
        oList.append(0)
    print(oList[i], end=" ")

