"""
求n的阶乘末尾有几个零。

注意点：

    将时间复杂度控制为log(n)

例子:

输入: n = 5

输出: 1
解题思路

通过因数分解知道，10是由2和5相乘得到的，而在n的阶乘中，因子2的数目总是比5多的，所以最终末尾有几个零取决于其中有几个5。1到n中能够整除5的数中有一个5，能整除25的数有2个5（且其中一个在整除5中已经计算过）…所以只要将n不断除以5后的结果相加，就可以得到因子中所有5的数目，也就得到了最终末尾零的数目。

"""
class Solution(object):
    def trailingZeros(self,n):
        count = 0
        while n:
             n //= 5
            count += 1
        return count
if __name__ == "__main__":
    print(Solution().trailingZeros(5))

