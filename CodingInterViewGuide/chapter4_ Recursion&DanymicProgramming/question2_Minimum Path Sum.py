'''
最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
同LeetCode64
https://leetcode-cn.com/problems/minimum-path-sum/
'''
def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid or not grid[0]:
        return None

    more = max(len(grid), len(grid[0]))
    less = min(len(grid), len(grid[0]))
    rowmore = (more == len(grid))
    arr = [100000] * less
    arr[0] = grid[0][0]
    for i in range(1, less):
        arr[i] = arr[i - 1] + (grid[0][i] if rowmore else grid[i][0])

    for i in range(1, more):
        arr[0] = arr[0] + (grid[i][0] if rowmore else grid[0][i])
        for j in range(1, less):
            arr[j] = min(arr[j], arr[j - 1]) + (grid[i][j] if rowmore else grid[j][i])

    return arr[-1]


print(minPathSum([[1,2,5],[3,2,1]]))
