import math

x = int(input())
a = list(input().split())
count = 0

for i in range(0, x - 1):
    if a[i + 1] > a[i]:
        count += 1

print(count)
