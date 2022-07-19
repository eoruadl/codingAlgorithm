import sys

n = int(sys.stdin.readline())

number = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    number.append(a)

for i in range(n):
    print(number[i][0]+number[i][1])
