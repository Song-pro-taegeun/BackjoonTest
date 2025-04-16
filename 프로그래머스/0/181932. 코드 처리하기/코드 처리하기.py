def solution(code):
    mode = 0
    ret = ""
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = not mode
            else: 
                if i % 2 == 0:
                    ret += code[i]
        else:
            if code[i] == "1":
                mode = not mode
            else: 
                if i % 2 == 1:
                    ret += code[i]
    if not ret:
        return "EMPTY"
    return ret