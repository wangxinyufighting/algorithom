'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现 两 次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1] 输出: 1
示例 2:
输入: [4,1,2,1,2] 输出: 4
'''

#相同的两个数字异或结果为0，则偶数个相同的数字异或结果为0，与那个只出现一次的数字异或，得到那个数字本身
class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for i in nums:
            result ^= i

        return result

    '''
    137. Single Number II
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现 三 次。找出那个只出现了一次的元素。
    '''
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        i = 1
        result = 0
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                if i + 3 < len(nums):
                    i += 3
                else:
                    result = nums[-1]
                    break
            else:
                result = nums[i - 1]
                break
        return result

    def singleNumber(self, nums) -> int:
        ones = 0
        twos = 0
        threes = 0
        for num in nums:
            # 用Int32位任意一位出现了一次1的结果ones 和当期num与 则同一个位置出现两次的会是1合并到twos 出现一次的保持twos原先的位
            twos |= ones & num
            # 一直异或num 则Int中的某一位出现一次1 ones为1 两次则异或成0 三次还是1 但是会被后续操作清零
            ones ^= num
            # ones和twos同时为1时 threes为1
            threes = ones & twos
            # threes对应的位置为1 取反为0 和ones与则将对应位清零
            ones &= ~threes
            twos &= ~threes
        return ones

    '''
        260. Single Number III
        给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
        思路：
            x，y表示两个只出现过一次的数字
            将nums中所有的全部异或一遍，得到x和y的异或值z。
            则二进制下的z中的1表明x和y这在这个位置上不同，在这个位置上，一个是1，另一个是0，谁是1谁是0不知道，也不用知道。
            随便找一个1来区分x和y。为了方便，取z中的最后一个1.通过z与~z+1相与可以得到。即z = z&(~z+1).
            此时，z变成了只有一个1的二进制数。
            重新遍历nums。
            当nums[i] & z == z时，说明nums[i]的那一位也是1.则通过异或给他恢复原样
            若不是，说明nums[i]的那一位不是1，就区分开了   
    '''
    def singleNumber(self, nums):
        result = [0]*2
        t = 0
        for i in range(len(nums)):
            t ^= nums[i]
        t &= (~t+1)
        for i in range(len(nums)):
            if t & nums[i] == t:
                result[0] ^= nums[i]
            else:
                result[1] ^= nums[i]

        return result
