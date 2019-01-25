"""
一个数组中和最大的子数组。

注意点：

    需要考虑负数的情况

例子：

输入: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

输出: 6(数组[4, -1, 2, 1]的和)
解题思路

又是比较经典的动态规划的题目。主要有以下几个概念，依次计算以第k个数作为子数组末尾的最优子数组（和最大）的和dp[]，然后求dp中的最大值。那递推关系是怎样的呢，当把下一个数字num[k+1]最为末尾数字时，要看它之前与它相连的子数组的和是否是正的，如果是正的，应该加上，否则舍弃。下面的代码把求dp和求dp中的最大值一起计算了，所以没有额外的数组dp。

现在还有一个疑问，就是num[k+1]之前与它相连的子数组应该定义为多长，它的起始位置是最靠近它的满足与这个数字相连的子数组的和为负的数字。如[-2, 1, -3, 4, -1, 2, 1, -5, 4]中-3前子数组的开端是1，-1是4，-5也是4。
"""
class Solution(object):
    def maxSubArray(self,nums):
        if not nums:
            return
        current = nums[0]
        length = len(nums)
        m = current
        for i in range(length):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(current,m)
        return m

if __name__ == "__main__":
    print(Solution().maxSubArray([2,3,-1,-3,5,4,4]))