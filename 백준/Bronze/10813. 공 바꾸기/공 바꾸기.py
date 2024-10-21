num, roopNum = list(map(int, input().split()))
n = [i+1 for i in range(num)]
for count in range(roopNum):
    i, j= list(map(int, input().split()))
    x = n[j-1]
    y = n[i-1]
    n[i-1] = x
    n[j-1] = y
print(*n)