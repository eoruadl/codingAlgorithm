dList = list(map(int, input().split()))

if dList[0] != dList[1] and dList[1] != dList[2] and dList[2] != dList[0]:
    print(max(dList) * 100)

for i in range(len(dList)):
    if dList.count(dList[i]) == 3:
        print(10000 + dList[i] * 1000)
        break
for i in range(len(dList)):
    if dList.count(dList[i]) == 2:
        print(1000 + dList[i] * 100)
        break

a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    print(10000 + a*1000)
elif a == b or b == c:
    print(1000 + b*100)
elif a == c:
    print(1000 + a*100)
else:
    print(max(a,b,c)*100)