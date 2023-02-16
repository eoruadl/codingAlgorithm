n = input()

numList = list(n)
result = int(numList[0])
numList.pop(0)

for i in numList:
    if result == 0 or result == 1:
        result = result + int(i)
    elif int(i) == 0 or int(i) == 1:
        result = result + int(i)
    else:
        result = result * int(i)


print(result)

result = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
