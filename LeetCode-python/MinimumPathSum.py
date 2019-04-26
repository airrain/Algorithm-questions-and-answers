"""
从一个矩阵的左上角出发到右下角，只能向右或向下走，找出哪一条路径上的数字之和最小。

注意点：

    所有数字都是非负的

例子：

输入: [ [1, 2, 4], [2, 4, 1], [3, 2, 1] ]

输出: 9
解题思路

思路跟 Unique Paths 相似，不过从计算到达该点有多少种走法转变为求最小和为多少。找出上面和左边格子的最小值加上当前格子中的数字即可。为了节省空间，把二维dp降为一维的，因为是求最优解，前面的中间值可以抛弃。
"""
class Solution(object):
    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])

        dp = [0 for __ in range(n)]
        dp[0] = grid[0][0]
        for j in range(1,n):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1,m):
            dp[0] += grid[i][0]
            for j in range(1,n):
                dp[j] = min(dp[j],dp[j - 1] + grid[i][j])
            return dp[-1]

if __name__ == "__main__":
     print(Solution().minPathSum([
            [1,2,4],
            [2,4,1],
            [3,2,1]]))
