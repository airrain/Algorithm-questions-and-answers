"""
格雷码表示在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同。现给定二进制码的位数，要求打印出格雷码序列。

注意点：

    格雷码序列有多种可能，可以先改变低位或高位

例子：

输入: n = 2

输出: [0,1,3,2]

00 - 0
01 - 1
11 - 3
10 - 2

解题思路

根据维基百科上的关于 格雷码和二进制数的转换关系 实现的代码
"""
class Solution(object):
    def grayCode(self,n):
        result = [(i >> 1) ^ i for i in range(pow(2,n)) ]
        return result

if __name__ == "__main__":
    print(Solution().grayCode(4))







