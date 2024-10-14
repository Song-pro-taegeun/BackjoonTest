n, check = map(int, input().split())
a = list(map(int, input().split()))
result = ""
for i in range(n):
    if(a[i] < check):
        result += str(a[i]) + " "

print(result)