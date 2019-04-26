"""
一共有n级楼梯，每次能够爬一级或两级，共有多少种不同的爬法爬到顶端。

注意点：

    无

例子：

输入: n = 6

输出: 13
解题思路

典型的动态规划题，递推表达式为 dp[i]=dp[i-1]+dp[i-2]，n为1时只有一种方法，n为2时有两种方法。
"""
class Solution(object):
    def climbStairs(self,n):
        if n <= 2:
            return n
        dp = [0 for __ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

if __name__ == "__main__":
    print(Solution().climbStairs(5))
