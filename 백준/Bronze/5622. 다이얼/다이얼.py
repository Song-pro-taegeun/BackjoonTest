dial = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", "OPERATOR"]

S = input()
countData = 0
sumData = 0
for i in S:
    for x in dial:
        countData += 1
        if x.find(i) > -1:
            if countData != 11:
                sumData += countData
    countData = 0            

print(sumData)