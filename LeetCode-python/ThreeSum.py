'''找出一个列表中所有和为零的三元组。要求求出的三元组中没有重复。
注意点：
   三元组中的数字要按增序排列(a<=b<=c)
   结果集中没有重复的三元组
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sorted array can save a lot of time
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) == 0:
                    result.append(l)
                    j += 1
                    k -= 1
                    # Ignore repeat numbers
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum(l) > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            # Ignore repeat numbers
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result
