import math

x = int(input())
a = list(input().split())
count = 0

def determine_this(n, arr):
    for i in range(0, n - 1):
        if (-1 * int(arr[i]) > 0 and -1 * int(arr[i + 1]) > 0) or (-1 * int(arr[i]) < 0 and -1 * int(arr[i + 1]) < 0):
            return True
    return False


print("YES" if determine_this(x, a) else "NO")
