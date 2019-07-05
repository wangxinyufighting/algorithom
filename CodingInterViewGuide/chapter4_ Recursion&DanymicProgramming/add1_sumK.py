'''
给定一个数组nums和数字k
求解从nums中挑选数字的和能否等于k
例：nums=[3,34,4,12,5,2], k=9
输出：True
解释：3+4+2=9或4+5=9
'''
def sumK(nums, K):
    subset = [[0]*(K+1) for _ in range(len(nums))]
    for i in range(K+1):
        subset[0][i] = 0 #False
    for i in range(len(nums)):
        subset[i][0] = 1 #True
    if nums[0] <= K:
        subset[0][nums[0]] = 1 #True

    for i in range(1, len(nums)):
        for k in range(K+1):
            if nums[i] > k:
                subset[i][k] = subset[i-1][k]
            else:
                subset[i][k] = subset[i-1][k] if subset[i-1][k] == 1 else subset[i-1][k-nums[i]]

    return True if subset[-1][-1] == 1 else False


print(sumK([3, 34, 4, 12, 5, 2], 13))
# x = [[1,2,3],[4,5,6],[7,8,9]]
# print(x[0])