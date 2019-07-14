'''
5127. 数组的相对排序
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
'''
class Solution:
    def relativeSortArray(self, arr1, arr2):
        if not arr1:
            return None
        if not arr2:
            return arr1

        sorted_ = []
        others = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    sorted_.append(j)
        for i in arr1:
            if i not in arr2:
                others.append(i)

        return sorted_ + sorted(others)

s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))