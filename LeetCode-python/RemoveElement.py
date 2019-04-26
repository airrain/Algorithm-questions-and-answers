"""
删除一个数组中某一特定数值的元素，返回删除后的数组长度。

注意点：

    操作结束后的数字排列顺序不需要与之前相同
    超出返回长度的部分不需要处理

例子：

输入: nums [1, 2, 3, 4, 3, 2, 1]，val = 1 输出: 5
解题思路

左右两个指针向中间靠拢，左指针找到一个等于val的值，右指针找到第一个不等于val的值，把右指针指向的值赋值给左指针。继续向中间靠拢。
"""
class Solution(object):
    def removeElement(self,nums,val):
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and left != val:
                left += 1
            while left <= right and right == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -=1
            return right + 1

if __name__ == "__main__":
    print(Solution().removeElement([1,3,4,2,6,3,5,2],2))
