num = int(input())
number = []
for i in range(num):
    a = list(map(int, input().split()))
    number.append(a)

for i in range(num):
    print(number[i][0]+number[i][1])