class Solution:
    '''
    写法1：不断选择元素
    '''
    def permute(self, nums):
        used = [False] * len(nums)
        result = []
        result = self.backtrack(nums, 0, [], used, result)
        return result

    def backtrack(self, nums, index, temp, used, result):
        #递归终止条件：index遍历到最后了
        if index == len(nums):
            result.append(temp.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                #选择元素
                used[i] = True
                temp.append(nums[i])
                self.backtrack(nums, index+1, used, result)
                #回溯
                used[i] = False
                temp.pop()

        return result

    '''
    写法1：不断交换元素
    '''
    def permute(self, nums):
        n = len(nums)
        if n < 1:
            return None

        result = []

        def backtrack(first):
            #递归终止条件：
            if first == n:
                result.append(nums)

            for i in range(first, n):
                #交换元素
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                #回溯：把元素放回原样
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return result















