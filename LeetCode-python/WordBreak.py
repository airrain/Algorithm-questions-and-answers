"""
给定一个目标字符串和一组字符串，判断目标字符串能否拆分成数个字符串，这些字符串都在给定的那组字符串中。

注意点：

    无

例子:

输入: s = "leetcode", wordDict = {"leet", "code"}

输出: True
解题思路

采用动态规划的方法解决，dp[i]表示字符串s[:i]能否拆分成符合要求的子字符串。我们可以看出，如果s[j:i]在给定的字符串组中，且dp[j]为True（即字符串s[:j]能够拆分成符合要求的子字符串），那么此时dp[i]也就为True了。按照这种递推关系，我们就可以判断目标字符串能否成功拆分。
"""
class Solution(object):
	def countAndSay(self,n):
		result = "1"
		for __ in range(1,n):
			result = self.getNext(result)

		return result

	def getNext(self,s):
		result = []
		start = 0
		while start < len(s):
			



