import sys

t = int(sys.stdin.readline())
array = []
for i in range(t):
    a, b = list(map(int, sys.stdin.readline().split()))
    array.append(a+b)
    
for i in range(len(array)):
    print(array[i])
    
