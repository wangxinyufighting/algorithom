'''
字符串中数字子串的和
'''
def numSum(str):
    if not str:
        return 0
    res = 0
    num = 0
    pos = True
    cur = 0
    for i in range(len(str)):
        if not str[i].isdigit():
            res += num
            num = 0
            if str[i] == '-':
                if i-1 > -1 and str[i-1] == '-':
                    pos = not pos
                else:
                    pos = False
            else:
                pos = True
        else:
            cur = int(str[i]) if pos else -int(str[i])
            num = num * 10 + cur
    res += num
    return res

print(numSum('---12a3'))