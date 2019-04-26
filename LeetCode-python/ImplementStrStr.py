"""
实现字符串子串匹配函数strStr()。如果字符串A是字符串B的子串，则返回A在B中首次出现的地址，否则返回-1。

注意点：

    空字符串是所有字符串的子串，返回0

例子：

输入: haystack = "abc", needle = "bc" 输出: 1

输入: haystack = "abc", needle = "gd" 输出: -1
解题思路

字符串匹配常见的算法是KMP，不过感觉该算法理解困难，效率也不是特别高。我用了Sunday算法来实现字符串的匹配。大体思路如下：

被搜索的字符串是"abcdefg"，要搜索的字符串是"ef"

 abcdefg
 ef

如果当前不匹配，则判断当前尝试匹配的后一位，即"c"是否在要搜索的字符串中，如果不在，则要搜索的字符串直接后移它自己的长度+1。

 abcdefg
    ef

如果存在，如此时"f"在"ef"中，则把该位置对齐。

 abcdefg
     ef

匹配成功返回结果。
"""
class Solution(object):
    def strStr(self,haystack,needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        needleLength = len(needle)
        while i < len(haystack):
            a = haystack()
