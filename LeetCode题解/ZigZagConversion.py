"""
将所给字符串按特定形状排列，依次将每排的字符连接形成新的字符串。具体看一个例子：给定字符串"PAYPALISHIRING"，相应排列成的形状如下：

P   A   H   N
A P L S I I G
Y   I   R

可以看出来是将字符串按照N的书写顺序重新排列了。现在要求我们从第一排开始依次把所有字符组成新的字符串："PAHNAPLSIIGYIR"

注意点：

    行数不是固定的

例子：

输入: s="PAYPALISHIRING", numRows=3 输出: "PAHNAPLSIIGYIR"
解题思路

发现其实新的字符串的顺序在原字符串中是有规律可循的。重新组合后的形状其实就是一个个N，相邻N对应位置之间的字符个数是固定的，如例子中的P-A-H-N之间的字符都是3个。现在假设行数为n，则对应位置字符间的间距都为2n-3，现在第一排和最后一排的字符顺序就可以确定了；但中间排的字符就比较特殊，在对应位置之间还会夹着一个字符。以例子中第一列的A和第二列的P来说，假设A的下标为i（从0开始），则A和P的间距为2(n-i-1)-1=2n-2i-3，而A和L的间距为2n-3，同时去掉P自己，所以P和L的间距为(2n-3)-(2n-2i-3)-1=2i-1。这样只需遍历第一列的字符，并依次加上对应的间距来获取后面的字符即可。上文的间距是指中间隔了几个字符。
"""
class Solution(object):
    def convert(self,s,numRows):
        if numRows <= 1:
            return s
        result = ''
        index = 0
        n = len(s)
        for i in range(0,numRows):
            if i == 0 or i == numRows - 1:
                while index < n:
                    result += s[index]
                    index += 2 * numRows - 2
                index = i + 1
            else:
                while index < n:
                    result += s[index]
                    index += 2 * numRows
                    if index >= n:
                        break
                    result += s[index]
                    index += 2 * i
                index = i + 1
            return result

if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING",2))




