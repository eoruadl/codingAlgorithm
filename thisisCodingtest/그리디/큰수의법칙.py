n, m, k = map(int, input().split())
data = list(map(int, input().split()))

a = sorted(data)

first = a[n-1]
second = a[n-2]

result = 0

while 1:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)