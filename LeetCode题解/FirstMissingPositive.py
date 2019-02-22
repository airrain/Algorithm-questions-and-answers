"""
找出一个无序数组中缺少的最小的正整数。

注意点：

    时间复杂度为O(n)
    只能使用常数级额外空间

例子：

输入: nums = [1, 2, 0] 输出: 3

输入: nums = [3,4,-1,1] 输出: 2
解题思路

由于只需要找出缺少的第一个正整数，我们不妨把所有正数放到对应的位置，再找到第一个位置不匹配的地方原本应该放哪个数。如上面的例子[1,2,0]就已经排列好了，而[3,4,-1,1]应变为[1,-1,3,4]。分别遍历这两个数组，找到nums[i]!=i+1的位置，如果所有位置都符合，说明所有的数组成了从1开始的连续正整数。进行排列的方法就是依次遍历每个数字，把它们放到应该放置的位子。
"""
class Solution(object):
	def firstMissingPositive(self,nums):
		if not nums:
			return 1
		i = 0
		length = len(nums)
		current = nums[i]
		if current <= 0 or current > length or nums[current - 1] == current:
			i += 1
		else:
			nums[current - 1],nums[i] = nums[i],nums[current - 1]
		for i in range(length):
			if nums[i] != i + 1:
				return i + 1
		return length + 1

if __name__ == "__main__":
	print(Solution().firstMissingPositive([1,3,5,4,-1]))
	
