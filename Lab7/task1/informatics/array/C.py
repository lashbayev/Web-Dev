import math

x = int(input())
a = list(input().split())
count = 0

for i in range(0, x):
    if int(a[i]) >= 0:
        print(a[i])
