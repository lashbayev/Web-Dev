
def xor(x, y):
    if x == 1 and y == 1:
        return False
    elif x == 0 and y == 0:
        return False
    return True

x, y = int(input()), int(input())

print(xor(x, y))
