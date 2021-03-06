"""
在一个有序数组中，如果目标数字存在，则返回它的下标，否则返回它应该插入位置的下标值。

注意点：

    数组中没有重复数字

例子：

输入: nums = [1, 3, 5, 6], target = 5 输出: 2

输入: nums = [1, 3, 5, 6], target = 2 输出: 1
解题思路

又是一道二分搜索的题。分以下几种情况：如果当前数字是目标数字，或者当前数字大于目标数字而它之前的数字小于目标数字，则返回当前下标；如果当前数字为最后一个且它比目标数字小，则返回当前下标的后一位。
"""
class Solution(object):
    def serachInsert(self,nums,target):
        length = len(nums)
        start = 0
        end = length
        while star < end:
            mid = (start + end) // 2
            if nums[mid] == target or nums[mid] > target

