"""
将一个字符串依照单词的力度进行反转。例如将"the sky is blue"转化为"blue is sky the"。

注意点：

    原始字符串中可能首位有空格，结果不要有这些空格
    原始字符串单词间可能有多个空格，结果单词间只需有一个空格

例子:

输入: s = "the sky is blue"

输出: "blue is sky the"
解题思路

用Python解决这个问题有些特殊，Python中的字符串是不可变的数据类型，而比较pythonic的写法是直接一行代码，先把字符串按空格分开，反转后用空格连接起来。

从算法层面讲，这道题希望做到原地完成字符串的反转。我们可以通过以下几步做到：

    将整个字符串直接反转
    遍历字符串单独将每个单词反转，注意反转的同时可以通过移位来除去不必要的空格

"""
class Solution(object):
	def reverseWords(self,s):
		return " ".join(s.split()[::-1])

if __name__ == "__main__":
	Solution().reverseWords("the sky is blue")


















