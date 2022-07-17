h, m = map(int, input().split())
num = int(input())
hnum = num // 60
mnum = num % 60
h = h + hnum
m = m + mnum
if m >= 60:
    h = h+1
    m = m - 60
if h >= 24:
    h = h -24
print(f"{h} {m}")
