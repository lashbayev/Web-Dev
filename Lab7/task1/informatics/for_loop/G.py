x = int(input())
d = int(input())

for i in range(x, d + 1):
    if d % i == 0:
        print(i)
        break
