#1

import numpy as np

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr += list(map(int, input().split()))
    
transformed = np.array(arr)
tr1 = np.reshape(transformed, (N, M))

print(np.mean(tr1, axis = 1))
print(np.var(tr1, axis = 0))
print(np.std(tr1, axis = None))

#2
import numpy

arr = list(map(int, input().split()))
transformed = numpy.array(arr)

print(numpy.reshape(transformed, (3, 3)))

#3
import numpy

def arrays(arr):
    transformed = numpy.array(arr, float)
    return transformed[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#4
import numpy as np
np.set_printoptions(legacy = '1.13') 

arr = list(map(float, input().split()))
transformed = np.array(arr)
print(np.floor(transformed))
print(np.ceil(transformed))
print(np.rint(transformed))

#5
import numpy as np

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr += list(map(int, input().split()))
    
transformed = np.array(arr)
tr1 = np.reshape(transformed, (N, M))
    
result = np.min(tr1, axis = 1)
print(np.max(result, axis = None))
#6
import numpy as np

N = int(input())
arr = []

for _ in range(N):
    arr += list(map(float, input().split()))

matrix = np.array(arr).reshape(N, N)
det = np.linalg.det(matrix)
print(round(det, 2))

#7
import numpy as np

arr = []
N, M = map(int, input().split())

for _ in range(N):
    arr += list(map(int, input().split()))
    
matrix = np.array(arr).reshape(N, M)
sum_arr = np.sum(matrix, axis = 0)
print(np.prod(sum_arr))

#8
def split_and_join(line):
    return "-".join(line.split(" "))
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#10
N = int(input())
countries = set()

for _ in range(N):
    countries.add(input())

print(len(countries))
