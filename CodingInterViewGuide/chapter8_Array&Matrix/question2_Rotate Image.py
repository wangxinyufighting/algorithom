'''
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
LeetCode 48
https://leetcode-cn.com/problems/rotate-image/

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image

'''
#--------------------------------------------------------------------------
'''
中心思想是：
根据矩阵的左上角（hx，hy）和右下角（tx，ty）确定一个矩阵（注意，不一定是方阵）
然后对于外圈，调整元素顺序
1 2 3    7 4 1 
4   6 -> 8   2
7 8 9    9 6 3
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None

        hx = 0
        hy = 0
        tx = len(matrix) - 1
        ty = len(matrix[0]) - 1
        while hx < tx and hy < ty:
            self.rotate_(matrix, hx, hy, tx, ty)
            hx += 1
            hy += 1
            tx -= 1
            ty -= 1
        return matrix

    def rotate_(self, matrix, hx, hy, tx, ty):
        times = tx - hx
        temp = 0
        for i in range(times):
            temp = matrix[hx][hy + i]
            matrix[hx][hy + i] = matrix[tx - i][hy]
            matrix[tx - i][hy] = matrix[tx][ty - i]
            matrix[tx][ty - i] = matrix[hx + i][ty]
            matrix[hx + i][ty] = temp