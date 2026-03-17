import math

x = int(input())
i = 1

while x > 0:
    i += 1
    if x % i == 0:
        print(i)
        break
