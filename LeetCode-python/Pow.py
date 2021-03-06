"""
求x的n次幂。

注意点：

    n是负数时需要取相反数

例子：

输入: x = 2, n = -1

输出: 0.5

输入: x = 2.1, n = 2

输出: 4.41
解题思路

最简答的方法就是把n个x直接做乘法，但这样要进行(n-1)次运算。现在以2**8(表示2的8次方)作为例子，需要进行7次乘法，但如果当做(2**2)**4->((2**2)**2)**2来计算就只要做3次乘法。即当n为奇数时，直接乘上当前的x，偶数时x变为x的平方，n除以2。这样就可以较快速的求出结果。当n为负数时要取倒数。
"""
class Solutiom(object):
    def myPow(self,x,n):
    	flag = 1 if n > 0 else -1
    	result = 1
    	n = abs(n)
    	while n > 0:
    		if n && 1 == 1:
    			result *= x
    		n >>= 1
    		x *= x
    	if flag < 0:
    		result = 1 / result
    	return result

if __name__ == "__main__":
	Solution().myPow(2,3)










