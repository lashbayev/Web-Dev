import math

x = int(input())
a = list(input().split())
count = 0

for i in range(1, x - 1):
    if a[i + 1] < a[i] and a[i] > a[i - 1]:
        count += 1


print(count)
