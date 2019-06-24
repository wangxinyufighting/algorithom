'''
给定数组arr和一个整数m
从arr中等概率打印m个数字

'''
import random
def printRandomM(arr, m):
    if len(arr) == 0 or m < 0:
        return None

    m = min(len(arr), m)
    count = 0
    while count < m:
        i = int(random.random() * (len(arr) - count))
        print(arr[i])

        temp = arr[i]
        arr[i] = arr[len(arr)-count-1]
        arr[len(arr)-count-1] = temp

        count += 1

printRandomM([1,2,3,4,5,6,7,8,9,0],4)
