"""
判断一个给出的数独模型是否符合要求。

注意点：

    该模型不需要填完整，没有填写的用"."表示
    不用关心该模型是否有解，只需要判断现有情况

例子：

输入: board=["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."] 输出: false
解题思路

用三个列表表示横向、纵向和小正方形的情况。特别需要注意的是小正方形内的元素的表示方法：board[i/3*3+j/3][i%3*3+j%3]。
"""
class Solution(object):
    def isValidSudoku(self,board):
        point = "."
        for i in range(9):
            row = []
            column = []
            square = []
            for j in range(9):
                element = board[i][j]
                if element != point:
                    if element in row:
















