"""问题1: 
	给定一个整数N，返回斐波那契数列的第N项？
"""

def fibonacci_1(n):
	if n < 0:
		raise ValueError("The n is illegall!")

	if n < 3:
		return 1

	return fibonacci_1(n - 1) + fibonacci_1(n - 2)

def fibonacci_2(n):
	if n < 0:
	raise ValueError("The n is Illegall!")

	if n < 3:
	return 1

    a,b = 1,1
    for _ in range(3,n+1):
    	tmp = a + b
    	a = b
    	b = tmp
    return tmp

def fibonacci_3(n):
	pass

"""问题2: 
	给定整数N，代表台阶数，一次可以跨2个或者1个台阶，返回有多少种走法？
"""
def getResult(n):
	if n < 0:
		raise ValueError("The n is Illegall!")

	if n < 3:
		return 1

	return getResult(n - 1) + getResult(n - 2)




