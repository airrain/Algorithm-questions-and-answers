"""给两个整型的有序数组，要求找出这两个数组中的中位数，时间复杂度为O(log (m+n))。

注意点：

    数组是有序的
    时间复杂度为O(log (m+n))
    考虑奇偶情况，如果总是为偶数，因返回中间的两个的平均数，且为float类型
    Python版本问题，部分Python3语法LeetCode好像不支持。

例子：

输入: num1=[1, 2], num2=[1, 2, 3] 输出: 2

输入: num1=[], num2=[2, 3] 输出: 2.5
"""
class Solution(object):
    def getMedianOfTwoSortedArrays(self,num1s,nums2):
        length1 = len(nums1)
        length2 = len(nums2)
        k = (length1 + length2) // 2
        if k % 2 == 0:
            return (self.findK(nums1,nums2,k) + self.finK(nums1,nums2,k - 1)) / 2.0
        else:
            return self.findK(nums1,nums2,k)


    def findK(self,num1,num2,k):
        if not num1:
            return num2[k]
        if not num2:
            return num1[k]
        if k == 0:
            return min(num1[0],num2[0])
        length1 = len(num1)
        length2 = len(num2)

if __name__ == '__main__':
    Solution().getMedianOfTwoSortedArrays([1,3,4],[2,4,5])

