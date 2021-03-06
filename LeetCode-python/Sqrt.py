"""
求一个数的平方根。

注意点：

    结果返回整数，舍去小数，不是四舍五入

例子：

输入: x = 5

输出: 2
解题思路

采用牛顿迭代法，通过逼近来求方程 $$y=x^2+a$$ 的解。接单介绍一下牛顿迭代法，如下图，求方程曲线与y轴的交点就是方程的解。随意取一个值 $$X0$$ ，找出曲线在 $$X$$ 处的切线，该切线与y轴的交点为 $$X1$$ ，再求 $$X1$$ 处的切线的交点，可以看出来交点会不断的向目标值靠近，现在确定一个阈值就可以找出近似解了。由于平方根是正数，所以初始的取值应为一个正数
"""
class Solution(object):
	def muSqrt(self,n):
		result = 1.0
		while abs(result * result - x) > 0.1:
			result = (result + x/result) / 2
		return int(result)

if __name__ == "__main__":
	Solution().mySqrt(5)
		