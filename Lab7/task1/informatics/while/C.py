import math

x = int(input())
i = 1

while math.pow(2, i) < x :
    print(int(math.pow(2, i)))
    i += 1
