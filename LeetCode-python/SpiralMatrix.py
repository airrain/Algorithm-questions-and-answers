"""
将一个矩阵中的内容螺旋输出。

注意点：

    矩阵不一定是正方形

例子：

输入: matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

输出: [1, 2, 3, 6, 9, 8, 7, 4, 5]
解题思路

控制好当前遍历的边界，不断的向内缩进。需要注意的是，缩到最里面的时候可能会出现以下几种情况：

中心剩下一个数值
———
|3|
———

中心横向多个数值
—————————
|3 4 5 6|
—————————

中心纵向多个数值
———
|2|
|3|
|4|
———

分别处理一下即可。
"""
class Solution(object):
    def spiralOrder(self,matrix):
        if not matrix:
            return []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = []
        while left < right and top < bottom:
            for i in range(left,right):
                result.append(matrix[top][i])
            for i in range(top,bottom):
                result.append(matrix[i][right])
            for i in range(right,left,-1):
                result.append(matrix[i][left])
            left += 1
            right += 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            result.append(matrix[top][left])
        elif left == right:
            for i in range(top,bottom + 1):
                result.append(matrix[i][left])
        elif top == bottom:
            for i in range(left,right + 1):
                result.append(matrix[top][i])
        return result

if __name__ == "__main__":
    Solution().spiralOrder([[1,2,3],
                            [4,5,6],
                            [7,8,9]])












