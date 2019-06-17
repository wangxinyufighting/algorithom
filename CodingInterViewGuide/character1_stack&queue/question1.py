'''
设计一个有getMin功能的栈
和LeetCode155 一样
    设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/min-stack
'''


#利用一个辅助栈来实现
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #stack用来实现基本的
        #min用来实现getMin功能, 对于min，所有操作的原则就是保证其栈顶元素最小
        self.stack = []
        self.min = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min or self.min[-1] >= x:
            self.min.append(x)


    def pop(self):
        """
        :rtype: None
        """
        temp = self.stack.pop()
        if temp == self.min[-1]:
            self.min.pop()
        return temp

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()