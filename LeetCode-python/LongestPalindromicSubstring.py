"""
找到一个字符串的最长回文子字符串，该字符串长度不超过1000，且只有唯一一个最长回文子串。

注意点：

    返回结果是整个子字符串，不是它的长度
    回文字符串要考虑奇偶的情况

例子：

输入: s="abae"
输出: aba

输入: s="abbae"
输出: abba
解题思路

依次把每一个字符当做回文字符串的中间字符，找到以该字符为中间字符的回文串的最大长度。分别对奇偶的情况进行讨论，接下来的关键就是对边界的把握，确保下标不要越界。当子串已经包含首字符或最后一个字符且此时还是回文串的时候，下标分别会向两边多移一位，需要补回来。
"""
class Solution(object):
    def longestPalindrome2(self,s):
        if not s:
            return
        n = len(s)
        if n == 1:
            return s
        l = 0
        r = 0
        m = 0
        c = 0
        b = True
        for i in range(0,n):
            for j in range(0,min(n - i,i + 1)):


