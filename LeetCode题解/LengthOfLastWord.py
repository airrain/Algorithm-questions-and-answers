"""
找出最后一个单词的长度。

注意点：

    忽略尾部空格
    不存在最后一个单词时返回0

例子：

输入: s = "Hello world"

输出: 5
解题思路

很简答的一道题，用Python内置函数一行就可以解决 len(s.strip().split(" ")[-1]) 。自己写了一下，从后到前先忽略掉空格，再继续遍历到是空格或者遍历结束，两个者之间就是最后一个单词的长度。
"""
class Solution(object):
    def lengthOfLastWord(self,s):
        length = len(s)
        index = length - 1
        while index >= 0 and s[index] == "":
            index -= 1
        temp = index
        while index > 0 and s[index] != "":
            index -= 1
        return temp - index

if __name__ == "__main__":
    print(Solution().lengthOfLastWord(" abc"))

