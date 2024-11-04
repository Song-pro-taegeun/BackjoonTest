listA = []
result = ""
for i in range(5):
    a = list(input())
    listA.append(a)
        
max_index = max(range(len(listA)), key=lambda i: len(listA[i]))
max_len = len(listA[max_index])

for j in range(max_len):
    for i in range(len(listA)):
        result += listA[i][j] if j < len(listA[i]) else ""

print(result)