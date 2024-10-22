S = input()
exArr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

for i in exArr:
    while i in S:
        S = S.replace(i, ' ', 1)  # 한 번씩 교체
        count += 1 # 교체 주기 별 카운트 증가

# 공백 제거 후 남은 문자 출력
S = S.replace(" ", "")
print(len(S) + count)  # 남은 문자열 길이와 교체한 패턴 수 합산