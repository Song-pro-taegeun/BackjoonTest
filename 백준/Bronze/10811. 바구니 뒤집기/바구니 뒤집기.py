num, roopNum = list(map(int, input().split()))
n = [i+1 for i in range(num)]

for i in range(roopNum):
    a, b = list(map(int, input().split()))
    sub_list = n[a-1:b] 
    sub_list.reverse()
    
    n[a-1:b] = sub_list
print(*n)