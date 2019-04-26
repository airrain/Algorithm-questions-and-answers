"""
一直线上站了N个孩子，每个孩子都有一个属于自己的数字，现在按照如下规则给孩子分发糖果：每个孩子至少有一个糖果；相邻的孩子中数字比较大的那个拿的糖果也比较多。求最少要发掉多少个糖果。

注意点：

    无

例子:

输入: ratings = [1, 2, 3, 2]

输出: 7
解题思路

从前往后遍历的时候，我们只考虑升序的序列，对于其中一段升序的序列，最理想的情况是按照1,2,3...这样分发糖果；而对于降序的序列，如果从后往前遍历就也变成升序的了。通过前序和后序遍历后，升序与降序的交接处那个点会有两个值，因为要比两边的孩子拿到的糖果都多，所以取较大的那个值。这时候得到的数组就是在满足题目要求前提下每个孩子拿到的最少的糖果数，返回它的和即可。
"""
class Solution(object):
	def candy(self,ratings):
		n = len(ratings)
		candy = [1] * n
		for i in range(1,n):
			if ratings[i] > ratings[i - 1]:
				candy[i] = candy[i - 1] + 1
		for i in range(n - 2,-1,-1):
			if ratings[i] > ratings[i + 1]:
				candy[i] = max(candy[i + 1],candy[i + 1] + 1)
			return sum[candy]

if __name__ == "__main__":
	Solution().candy({1,2,3,7,4,3,2,1})