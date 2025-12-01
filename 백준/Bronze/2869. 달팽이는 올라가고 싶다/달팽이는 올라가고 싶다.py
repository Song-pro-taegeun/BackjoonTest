a, b, v = map(int, input().split())

# 정상에 도달하기 전까지 필요한 높이
need = v - a

# 하루에 실제로 오르는 양
per_day = a - b

# 필요한 일수 = need / per_day 의 올림값
days = (need + per_day - 1) // per_day + 1

print(days)