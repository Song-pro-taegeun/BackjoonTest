S = list(input())
M = 'abcdefghijklmnopqrstuvwxyz'

result = ""
for i in M:
    if i in S:
        result += str(S.index(i)) + " "
    else :
        result += "-1 "

print(result)