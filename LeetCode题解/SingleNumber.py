"""
一个数组中除了一个数字出现过一次外，其余的数字都出现了两次，找出那个只出现一次的数字。

注意点：

    算法时间杂度要求为O(n)
    空间复杂度为O(1)

例子:

输入: nums = [1, 2, 3, 4, 3, 2, 1]

输出: 4
解题思路

非常常见的一道算法题，将所有数字进行异或操作即可。对于异或操作明确以下三点：

    一个整数与自己异或的结果是0
    一个整数与0异或的结果是自己
    异或操作满足交换律，即a^b=b^a

所以对所有数字进行异或操作后剩下的就是那个只出现一次的数字。
"""
class Solution(object):
	def singleNumber(self,nums):
		result = nums[0]
		for i in nums[1:]:
			result ^= i
		return result
if __name__ == "__main__":
	Solution().singleNumber([1,2,3,4,3,2,1])

		