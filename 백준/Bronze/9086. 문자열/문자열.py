n = int(input())
result = []
for i in range(n):
    inStr = input()
    inStr = inStr[0] + inStr[len(inStr) -1]
    result.append(inStr)
    
print(*result)
    