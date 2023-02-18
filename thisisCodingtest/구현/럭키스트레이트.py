n = int(input())

data = str(n)
mid = int(len(data)/2)

firstList = []
secondList = []
for i in data[0:mid]:
    firstList.append(int(i))

for i in data[mid:]:
    secondList.append(int(i))

if sum(firstList) == sum(secondList):
    print("LUCKY")
else:
    print("READY")
