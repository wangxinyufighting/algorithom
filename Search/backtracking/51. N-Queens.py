'''
n皇后问题。回溯法。
'''
class Solution:
    def solveNQueens(self, n):
        arranged = self.queen(n)
        result = []

        for i in arranged:
            temp = []
            for j in range(n):
                r = ''
                k = 0
                while k < n:
                    if k == int(i[j]):
                        r += 'Q'
                    else:
                        r += '.'
                    k += 1
                temp.append(r)
            result.append(temp)
        return result

    def conflict(self, current, arranged):
        length = len(arranged)
        #has conflict is True
        flag = False
        for index in range(length):
            '''
            此处为了防止出现已出现的皇后的对角线上。
            随着index的增加，对角线的数值越来越小。
            即对于目前要放的皇后，他上一行的皇后的对角线是该皇后的位置±1；
            而他上上一行的皇后的对角线是该皇后的位置±2；
            以此类推，即是length-index的来历
            '''
            if abs(current - int(arranged[index])) in (0, length - index):
                flag = True
                break

        return flag

    def queen(self, n):
        result = []

        def backtrack(arranged):
            #够n个皇后了，就把这个答案搜集起来
            if len(arranged) == n:
                result.append(arranged)
                return

            for i in range(n):
                #检测位置是否会冲突，若不冲突就接着放下去；
                #若冲突，则回溯到上一层，选个别的接着试
                if not self.conflict(i, arranged):
                    backtrack(arranged + str(i))

        backtrack('')
        return result

s = Solution()
print(s.solveNQueens(4))