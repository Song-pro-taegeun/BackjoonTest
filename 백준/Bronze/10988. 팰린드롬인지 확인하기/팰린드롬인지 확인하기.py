S = list(input())
reverse_S = S[::-1]

tF = ""
for i in range(len(S)):
    if S[i] != reverse_S[i]:
        tF=0
        break
    else:
        tF=1
        
print(tF)