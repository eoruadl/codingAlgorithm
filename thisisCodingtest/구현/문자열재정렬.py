s = input()

alp = []
num = []
for i in s:
    if i.isdigit():
        num.append(int(i))
    else:
        alp.append(i)

alp.sort()
sumNum = sum(num)
sumAlp = "".join(alp)

print(sumAlp + str(sumNum))
