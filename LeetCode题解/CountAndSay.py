"""
把一个数字用几个几的形式表示出来。如2就是1个2，即12。对12进行数数得到1112，依次类推。假设初始数字是1，求第n个数是什么。起始5个数字为1, 11, 21, 1211, 111221, ...

注意点：

    题目中的数字都用字符串表

例子：

输入: n = 5 输出: 111221
解题思路

用一个下标来表示当前统计的字符的起始位置，一个计数器来表示该字符的数目。不断读取直到字符不相等，添加到结果集中，更新起始位置和计数器。下面代码中的计数器用下标相减代替。
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
			curr = start + 1
			while curr < len(s) and s[start] == s[curr]:
				curr += 1
			result.extend(str(curr - start),s[start])
			start = curr
		return "".join(result)

if __name__ == "__main__":
	Solution().countAndSay(4)
