a = [1, 1, 2, 2, 2, 8]
num = list(map(int,input().split()))

# zip() 각 배열의 요소를 튜플 형태로 가공
result = [x - y for x, y in zip(a, num)]
print(*result)