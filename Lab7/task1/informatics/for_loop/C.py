import math

a, b = int(input()), int(input())
for n in range(a, b + 1):
    if n >= 0 and int(math.isqrt(n)) ** 2 == n:
        print(n)
