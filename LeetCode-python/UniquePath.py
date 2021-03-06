"""
机器人从起点到终点有多少条不同的路径，只能向右或者向下走。

unique-path

注意点：

    格子大小最大为100*100

例子：

输入: m = 3, n = 7

输出: 28
解题思路

很常见的小学生奥数题，可以用排列组合来求解，一共要走(m-1)+(n-1)步，其中(m-1)步向下，(n-1)向右，且有公式 mCn = n!/m!(n-m)!
"""
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1 for __ in range(n)] for __ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[m - 1][n - 1]

"""import math
class Solution(object):
    def uniquePaths(self,m,n):
        m -= 1
        n -= 1
    return math.factorial(m + n) / (math.factorial(m) * math.factorial(n))

if __name__ == "__main__":
    Solution().uniquePaths(3,4)
    """

if __name__ == "__main__":
     print(Solution().uniquePaths(3,7))
