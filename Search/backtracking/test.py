def conflict(arranged, current):
    length = len(arranged)
    # has conflict is True
    flag = False
    for index in range(length):
        if abs(current - int(arranged[index])) in (0, length - index):
            flag = True
            break

    return flag

def queens0(num=3):
    for i in range(num):
        if not conflict([], i):
            for j in range(num):
                if not conflict([i], j):
                    for k in range(num):
                        if not conflict([i,j],k):
                            for m in range(num):
                                if not conflict([i,j,k],m):
                                    print ([i,j,k,m])

queens0()