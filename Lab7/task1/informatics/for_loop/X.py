import math

x = input()
decimal = 0

for i in range(len(x)-1, -1, -1):
    decimal += int(x[i]) * int(math.pow(2, len(x)-1-i))

print(decimal)
