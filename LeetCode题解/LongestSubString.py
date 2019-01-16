"""找出一个字符串的最长字符串，要求该字符串中没有重复的字符。

注意点：

    考虑空字符等特殊情况

例子：

输入: "abcabcbb" 输出: 3

输入: "bbbbbb" 输出: 1
"""
class Solution(object):
	def lengthOfLongestSubString(self,s):
		if not s:
			return 0
		if len(s) <= 1:
			return len(s)




