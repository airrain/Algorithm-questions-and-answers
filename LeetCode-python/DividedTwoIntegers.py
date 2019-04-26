"""
实现两个int型数字的除法，不可以使用乘法、除法和模操作。

注意点：

    如果结果溢出int类型，返回MAX_INT
    注意负数情况

例子：

输入: dividend = 5, divisor = -1 输出: -5
解题思路

可以先把符号抽取出来，只考虑两个正数相除的情况。除法其实就是被减数不断减去减数的操作，但直接不断进行减法会超时，应尽量减去大的数字，通过位移操作来快速找到比被减数小一些的减数的倍数current。不断减去且缩小current。溢出只可能是向上溢出，通过min操作进行过滤。
"""
class Solution(object):
    def divide(self,dividend,divisor):
        MAX_INT = 2147483647
        sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        current = divisor
        currentResult = 1
        while current <= dividend:
            current <<= 1
            currentResult <<= 1
        while divisor <= dividend:
            current >>= 1
            currentResult >>= 1
            if current <= dividend:
                dividend -= current
                result += currentResult
        return min(sign * result,MAX_INT)

if __name__ =="__main__":
    print(Solution().divide(5,1))
