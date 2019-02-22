"""
一个由包含一串数字的列表组成的非负整数加上一。

注意点：

    列表前面的数字表示高位
    注意最高位也可能进位

例子：

输入: [1, 2, 3, 4, 9]

输出: [1, 2, 3, 5, 0]
解题思路

从低位到高位，如果后一位有进位的话，那么该位要加上一，否则退出循环。如果最高位也进位，那么在列表前要插入一个一。
"""
class Solution(object):
    def plusOne(self,digits):
        carry = 1
        for i in range(len(digits) - 1,-1,-1):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] -= 10
        if carry == 1:
            digits.insert(0,1)
        return digits

if __name__ == "__main__":
    print(Solution().plusOne([1,2,3,4,9]))





