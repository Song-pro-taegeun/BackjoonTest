basicArray = [[0]*100 for i in range(100)]

n = int(input()) # 색종이 갯수
coordinateArr = [] # 좌표 배열

for i in range(n):
  line = []
  x, y = map(int, input().split()) # 좌표
  line.append(x)
  line.append(y)
  
  coordinateArr.append(line)
  
# 색종이 붙이기
for x, y in coordinateArr:
  for i in range(x, min(x+10, 100)):
    for j in range(y, min(y+10, 100)):
      basicArray[i][j] = 1

answer = sum(sum(row) for row in basicArray)
print(answer)