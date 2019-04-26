"""
在一个数组中找出一个子数组，使得子数组中的数的乘积最大。

注意点：

    数字可能为负数
    给定的数组不为空

例子:

输入: nums = [2,3,-2,4]

输出: 6
解题思路

比较典型的动态规划题目，需要注意负数乘以负数为正数，所以要同时记录最大局部最优解和最小局部最优解。递推关系式为：

temp = positive
positive = max(num, positive * num, negative * num)
negative = min(num, temp * num, negative * num)

    变量命名有点问题，positive指局部最大乘积（不一定是正数），negative指局部最小乘积（也不一定是负数）。
"""
class Sulution(object):
	def maxProduct(self,nums):
		positive,negative = nums[0],nums[0]
		result = nums[0]
		for num in nums[1:]:
			positive,negaive = max(num,positive * num,negative * num),min(num,positive * num,negative * num)
			result = max(result,positive)
		return result

if __name__ == "__main__":
	Solution().maxProduct([2,3,-2,5])