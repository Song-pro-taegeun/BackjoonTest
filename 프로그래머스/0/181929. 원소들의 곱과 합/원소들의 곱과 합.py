def solution(num_list):
    gop = 1
    square = 0
    for num in num_list:
        gop = gop*num
        square += num
    if gop > square ** 2:
        return 0
    else:
        return 1