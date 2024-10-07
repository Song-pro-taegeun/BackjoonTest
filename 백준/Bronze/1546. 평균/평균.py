n = int(input()) # 변수 받기
score = list(map(int, input().split())) # 변수 받기 -> 공백기점 분리
maxscore = max(score) # 최대값 추출

nscore = [i*100 / maxscore for i in score] # 리스트 -> 스코어 x 100 / 최대값 
print(sum(nscore) / len(nscore)) # 각 리스트 점수 합산 / 점수 갯수 
