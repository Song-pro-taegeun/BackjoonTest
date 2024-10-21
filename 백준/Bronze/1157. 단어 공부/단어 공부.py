S = input().upper()
arr = list(set(S))

cnt = []
for i in arr:
    cnt.append(S.count(i))
    
# cnt에서 max값을 추출하는 것을 카운트
# max 값이 1개를 초과한다면,
if cnt.count(max(cnt)) > 1 :
    print("?")
else: 
    # 문자열 배열에서 cnt 배열의 최대값을 구한 인덱스를 넘긴다.
    print(arr[cnt.index(max(cnt))])