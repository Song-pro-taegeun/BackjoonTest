N = int(input())
result = 0

for a in range(N):
    inputStr = input()
    seen = set()
    is_group= True
    
    prev = ""
    for ch in inputStr:
        if ch != prev:
            if ch in seen:
                is_group = False
                break
            seen.add(ch)
        prev = ch
        
    if is_group:
        result += 1


print(result)
