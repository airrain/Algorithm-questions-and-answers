"""
在Excel中，列名的表示形式为A,B,C…AA,AB…，给定一个Excel的列名，将其转化为数字，其中A表示1，其后以此类推。

注意点：

    无

例子:

输入: s = ‘A’

输出: 1

输入: s = ‘AB’

输出: 28
解题思路

相当于将一个二十六进制的数字转换为十进制，不过这里的二十六进制比较特殊，不是由1,2,3…A,B,…Q这些数字表示，而是A,B,C…Z来表示。但原理是一样的，同一个字母往左移一位，它表示的数字就变为原来的26倍。将每个字母根据它所在的位置计算出它表示的值即可。

"""
class Solution(object):
    def titleToNumber(self,s):
        base = ord('A') - 1
        n = len(s)
        result = 0
        for i in range(n):
            result += (ord(s[n - 1 - i]) - base)*pow(26,i)
        return result
if __name__ == "__main__":
    print(Solution().titleToNumber('AB'))

