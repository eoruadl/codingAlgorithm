a,b = map(int, input().split())
nList = list(map(int, input().split()))

for i in range(a):
    if nList[i] < b:
        print(nList[i], end= " ")