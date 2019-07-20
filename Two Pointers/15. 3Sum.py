class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for start in range(len(nums)-2):
            if nums[start] > 0:
                break
            if start > 0 and nums[start-1] == nums[start]:
                continue
            i, j = start+1, len(nums)-1
            while i < j:
                sum = nums[start] + nums[i] + nums[j]
                if sum == 0:
                    result.append([nums[start], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif sum > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
        return result

s = Solution()
print(s.threeSum([-2,0,1,1,2]))
