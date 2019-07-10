'''
n个人要在夜里过河；河上有座桥，每次只能通过两个人；过河需要手电筒，手电筒只有一个。
一次过河时间为两人中的走得慢的人的过河时间。
即需要两个人过河，一个人上岸后，另一个人把手电筒送回来。
t[i]表示第i个人过河的时间。
问最短的过河时间。

POJ 1700 http://poj.org/problem?id=1700
'''

'''
首先，情况特殊，把t数组升序排序。t[0]为耗时最少的。
设人从A渡河到B.
子问题为 A剩下几个人：1个还是2个。
因为剩下3个人可以拆解为以上情况的子问题。
f[i]表示i个人渡河的最短时间（所以肯定不包括最后一次把手电筒送回去的时间）

1、如果i-1人在B，1个人在A。
    手电筒在B，让那个跑的最快的送过来，花费t[0]；
    和i一起过河，花费t[i]；
    所以总计花费为f[i-1]+t[0]+t[i]
    
2、如果i-2人在B，2人在A。
    手电筒在B，让那个跑的最快的送过来，花费t[0]；
    此时A有3个人，让除了0以外的两个人过河，花费时间t[i]；
    让跑的第二快的人把手电筒送回来，花费t[1]；
    1和0一起渡河，花费t[1]。
    *若让跑的快的人陪i和i-1渡河，则时间太慢，花费为t[i]+t[0]+t[i-1]。
'''
def crossRiver(t):
    if not t:
        return 0
    f = [0]*len(t)
    sortedT = sorted(t)
    f[0] = sortedT[0]
    f[1] = sortedT[1]

    for i in range(2, len(t)):
        f[i] = min(f[i-1]+t[0]+t[i], f[i-2]+t[0]+t[i]+2*t[1])

    return f[-1]

print(crossRiver([1,2,5,10]))