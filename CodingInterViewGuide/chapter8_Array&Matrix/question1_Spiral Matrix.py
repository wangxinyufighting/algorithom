'''
转着圈打印一个矩阵
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

LeetCode54
https://leetcode-cn.com/problems/spiral-matrix/
'''
#--------------------------------------------------------------------------
'''
中心思想是：
根据矩阵的左上角（hx，hy）和右下角（tx，ty）确定一个矩阵（注意，不一定是方阵）
然后循环打印这个矩阵的外圈，打印完之后，hx++，hy++，tx--，ty--
在打印下一圈，直到右下角和左上角重合
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix

        hx = 0
        hy = 0
        tx = len(matrix) - 1
        ty = len(matrix[0]) - 1
        result = []
        while hx <= tx and hy <= ty:
            self.printSpiralMatrix(matrix, hx, hy, tx, ty, result)
            hx += 1
            hy += 1
            tx -= 1
            ty -= 1
        return result

    def printSpiralMatrix(self, matrix, hx, hy, tx, ty, result):
        if hx == tx and hy != ty:
            for i in range(hy, ty + 1):
                result.append(matrix[hx][i])
        elif hy == ty and hx != tx:
            for i in range(hx, tx + 1):
                result.append(matrix[i][hy])
        else:
            for i in range(hy, ty + 1):
                result.append(matrix[hx][i])
            for i in range(hx + 1, tx + 1):
                result.append(matrix[i][ty])
            for i in range(ty - 1, hy - 1, -1):
                result.append(matrix[tx][i])
            for i in range(tx - 1, hx, -1):
                result.append(matrix[i][hy])



