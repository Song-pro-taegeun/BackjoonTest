a, b = map(str, input().split())
aList = list(a)
aList.reverse()

bList = list(b)
bList.reverse()

aResult = ''.join(aList)
bResult =  ''.join(bList)
print(aResult if aResult > bResult else bResult)
