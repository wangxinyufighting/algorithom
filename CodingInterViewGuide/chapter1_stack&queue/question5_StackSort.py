'''
双栈排序

牛客：
https://www.nowcoder.com/practice/d0d0cddc1489476da6b782a6301e7dec?tpId=8&tqId=11009&tPage=1&rp=1&ru=/ta/cracking-the-coding-interview&qru=/ta/cracking-the-coding-interview/question-ranking

请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），
要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。

给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请返回排序后的栈。
请注意这是一个栈，意味着排序过程中你只能访问到最后一个元素。

测试样例：
[1,2,3,4,5]
返回：[5,4,3,2,1]
'''
# -*- coding:utf-8 -*-
def twoStacksSort(numbers):
    if len(numbers) == 0:
        return None

    help = []
    while len(numbers) != 0:
        cur = numbers.pop()
        while len(help) != 0 and help[-1] > cur:
            numbers.append(help.pop())
        help.append(cur)

    while len(help) != 0:
        numbers.append(help.pop())

    return numbers

t = twoStacksSort([1,2,3,4,5])
print(t)