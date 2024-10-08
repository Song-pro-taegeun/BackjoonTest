H, M = list(map(int, input().split()))

# M이 45보다 작으면 
if M < 45: 
    if H == 0: # H가 0시라면 23으로 바꿔준다
        H=23
        print(H, M+15) # 이후 M+15 후 출력
    else:
        print(H-1, M+15) # 0시가 아니라면 H-1, M+15
else:
    print(H, M-45) # M이 45보다 크면