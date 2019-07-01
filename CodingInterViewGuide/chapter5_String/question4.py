'''
判断旋转词
str1:abcdefg
str2:efgabcd
实际上是判断str2是否是由str1旋转（循环）而来
首先2*str2，即efgabcdefgabcd， 然后使用KMP算法在efgabcdefgabcd找到是否存在abcdefg
存在即是，不存在就不是
'''



'''
变种：给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串

右循环：
输入:  str="abcdefg", offset = 3
输出:  str = "efgabcd"	

左循环：
输入:  str="abcdefg", offset = 3
输出:  str = "defgabc"

'''
#右循环：
def rotateString(s, offset):
    # write your code here
    double = list(s) * 2
    if offset >= len(s):
        offset = offset - len(s)

    result = double[len(s) - offset: 2 * len(s) - offset]
    r = ''
    for i in result:
        r += i

    return r

#左循环：
def LeftRotateString( s, n):
    # write code here
    double = list(s) * 2
    if n >= len(s):
        n = n - len(s)

    result = double[n: len(s) + n]
    r = ''
    for i in result:
        r += i

    return r
