"""翻转一个intger类型的数字。

注意点：

    注意末尾有0的情况不能直接当作字符串翻转
    有正负两种情况
    integer是32位整型，考虑溢出

例子：

输入: x=123 输出: 321

输入: x=-123 输出: -321
"""
class Solution(object):
    def reverse(self,x):
        flag = 0
        if x < 0:
            flag = -1
        else:
            flag = 1
        x *= flag
        result = 0
        result = result * 10 + x % 10
        x /= 10
        if result > 2147483647:
            return 0
        return result * flag

if __name__ == '__main__':
    assert Solution().reverse(123)
    assert Solution().reverse(-123)
