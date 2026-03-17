import math

x = int(input())
count = 0

while(x > 0):
    x -= 1
    i = int(input())
    if i == 0:
        count += 1
        
print(count)
