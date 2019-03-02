"""
在一个每行从左到右依次递增，且下一行第一个数字比上一行最后一个数字大的矩阵中，判断目标数字是否存在。

注意点：

    无

例子：

输入:

matrix =
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3

输出: True
解题思路

把矩阵从左到右、从上到下连起来就是一个递增的数组，可以用二分搜索来查找。现在只要找出数组下标到矩阵的映射关系就可以了：i -> [i // n][i % n]，其中i是数组中的下标，n是矩阵的宽。
"""
class Solution(object):
    def searchMatrix(self,matrix,target):
        m = len(matrix)
        n = len(matrix[0])
        l,h = 0,m * n - 1
        while l <= h:
            mid = 1 + (h - 1) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                h = mid - 1
    return False

if __







