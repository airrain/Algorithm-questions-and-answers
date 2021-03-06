"""
给定两个字符串S和T，求T有多少种从属于S的子序列的情况。或者说S可以删除它自己任意个字符，但是不能改变字符的相对位置，那一共有多少种删法可以使S变为T。

注意点：

    删除任意个字符包括不删除字符

例子:

输入: s = "rabbbit", t = "rabbit"

输出: 3
解题思路

典型的动态规划问题，dp[i][j]表示字符串S[:i]和T[:j]的不同子序列数目，如果S[i-1]和T[j-1]不相等，那么只能在S[:i-1]和T[:j]中匹配，即dp[i][j] = dp[i-1][j]；而当S[i-1]和T[j-1]相等时，可以是这两个字符正好匹配，也可以忽略S[i-1]，使T[j-1]在S[:i-1]中匹配，所以dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]。进一步观察可以将二维数组压缩为一维，只需要从后往前计算即可。
"""
class Solution(object):
    def numDistinct(self,s,t):
        m = len(s)
        n = len(t)
        dp = [0 for __ in range(n + 1)]
        dp[0] = 1
        for i in range(m):
            for j in range(n - 1,-1,-1):
                if t[j] == s[i]:
                    dp[j + 1] += dp[j]
        return dp[-1]

if __name__ == "__main__":
    print(Solution().numDistinct("rabbbit","rabbit"))