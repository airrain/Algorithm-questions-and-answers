"""
用O(k)的空间得到杨辉三角第k行的数值。

注意点：

    从0开始计算行数，即第0行为[1]

例子:

输入: k = 3

输出: [1,3,3,1]

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

    1
    2
    3
    4
    5
    6
    7

解题思路

现在要考虑的是在 Pascal’s Triangle 的基础上节约空间，我们可以知道第k行需要(k+1)的空间，且下一行占用的长度都比上一行长，所以在计算下一行的值时适合从后往前计算。

"""
class Solution(object):
    def getRow(self,rowIndex):
        result = [1] * (rowIndex + 1)
        for i in range(2,rowIndex + 1):
            for j in range(1,i):
                result[i -j] += result[i - j - 1]
        return result
if __name__ == "__main__":
    print(Solution().getRow(3))









