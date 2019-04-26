"""
在一个有序的数组中找到找到目标数字的起始坐标和结束坐标，如果不存在则返回[-1, -1]。

注意点：

    时间复杂度为log(n)

例子：

输入: nums = [5, 7, 7, 8, 8, 10], target = 8 输出: [3, 4]

输入: nums = [5, 7, 7, 8, 8, 10], target = 6 输出: [-1, -1]
解题思路

通过两次二分法来获的两个边界，左边界的标志是中间数字为目标数字且它前面的数字不存在或不是目标数字；右边界的标志是中间数字为目标数字且它后面的数字不存在或不是目标数字。如果没有找到左边界就可以确定不存在目标数字。需要注意边界的操作。
"""
class Solution(object):
    def searchRange(self,nums,target):
        result = []
        length = len(nums)

        start = 0
        end = length
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target and (mid == 0 or nums[mid -1] != target):
                result.append(mid)
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if not result:
            return [-1,-1]

        end = length
        while start <  end:
            mid = (start + end) // 2
            if nums[mid] == target and (mid == length -1 or nums[mid + 1] != target):
                result.append(mid)
                break
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return result

if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10],8))









