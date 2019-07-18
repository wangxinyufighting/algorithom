'''
这个题和46.Permutations相似，不同点在于集合中出现重复元素。
对于重复元素，要做的是：
    1、排序；
    2、剪枝，避免重复计算
其余和不重复的情况一样
'''
class Solution:
    '''
    方法1：不断选择数据
    '''
    def permuteUnique(self, nums):
        if not nums:
            return []
        nums.sort()
        used = [False] * len(nums)
        result = []
        self.backtrack(nums, 0, [], used, result)
        return result


    def backtrack(self, nums, index, temp, used, result):
        if index == len(nums):
            #注意这里的copy，不然会是[]
            result.append(temp.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                temp.append(nums[i])
                self.backtrack(nums, index+1, temp, used, result)
                used[i] = False
                temp.pop()

    '''
    方法2：不断交换数据
    '''

    def permuteUnique1(self, nums):
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        result = []


        def backtrack(first):
            used = {}
            for i in nums:
                used[i] = False
            if first == n:
                result.append(nums)
            for i in range(first, n):
                if used[nums[i]]:
                    continue
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first+1)
                nums[i], nums[first] = nums[first], nums[i]
                used[nums[i]] = True

        backtrack(0)
        return result


s = Solution()
print(s.permuteUnique([1,1,2]))






