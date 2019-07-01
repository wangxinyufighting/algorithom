'''
去掉字符串中连续出现的k个0的子串

例如，A0000B000 k=3 输出 A0000B
'''

def removeZero(str, k):
    if not str or k < 1:
        return None

    start = -1
    count = 0
    str = list(str)

    for i in range(len(str)):
        if str[i] == '0':
            count += 1
            start = i if start == -1 else start
        else:
            if count == k:
                while count != 0:
                    str[start] = 0
                    start += 1
                    count -= 1

            count = 0
            start = -1

    if count == k:
        while count != 0:
            str[start] = 0
            start += 1
            count -= 1

    result = ''
    while str:
        t = str.pop(0)
        if t != 0:
            result += t

    return result


str = 'A0000B000C000'
s = removeZero(str, 3)
print(s)