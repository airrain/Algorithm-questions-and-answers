"""
输入三个字符串s1、s2和s3，判断第三个字符串s3是否由前两个字符串s1和s2交替而成且不改变s1和s2中各个字符原有的相对顺序。

注意点：

    无

例子：

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

输出: True
解题思路

典型的二维动态规划题目，dp[i][j]表示s1[:i+1]和s2[:j+1]能否交替组成s3[:i+j+1]，两个空字符串可以组成空字符串，所以dp[0][0]为True。边界的情况是一个字符串为空，另一个字符串的头部是否与目标字符串的头像相同。而在一般情况下，只有当以下两种情况之一成立时dp[i][j]为True：

    s1[i] == s3[i+j]，而且dp[i-1][j]为True
    s2[j] == s3[i+j]，而且dp[i][j-1]为True

递推关系式是：dp[i + 1][j + 1] = (dp[j + 1][i] and s1[i] == s3[i + j + 1]) or (dp[j][i + 1] and s2[j] == s3[i + j + 1])

考虑到不同纬度间的数据不干扰，所有可以把二维dp降为一维。
"""
class Solution(object):
    def isInterleave(self,s1,s2,s3):
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        dp = [True for __ in range(m + 1)]
        for i in range(m):
            dp[i + 1] = dp[i] and s1[i] == s3[i]
        for j in range(n):
            dp[0] = dp[0] and s2[j] == s3[j]
            for i in range(m):
                dp[i + 1] = (dp[i] and s1[i] == s3[i + j + 1]) or (dp[i +1] and s2[j] == s3[i + j + 1])
            return dp[m]

if __name__ == "__main__":
    print(Solution().isInterleave("aabcc","abbca","aadbbcbcac"))











