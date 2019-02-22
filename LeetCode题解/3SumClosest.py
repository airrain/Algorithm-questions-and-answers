"""\
找出一个列表中三个元素之和与目标值最接近的情况，并返回这个值。假设整个列表中只有一个最接近的值。

注意点：

    结果要求返回的是和，而不是三元组

例子：

输入: nums=[1, 1, 1, 1], target=-100 输出: 3
解题思路

思路与3Sum基本相同，现在要额外维护一个表示之前三元组中与目标值的差最小值的变量，这个变量的初始化值应该很大，防止把有意义的三元组直接排除了。此外，由于题目中明确说只有唯一的一组最优解，所有不用考虑重复数字了。
"""
class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        i = 0
        result = 0
        distance = pow(2,32) - 1
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)
            while j < k:
                l = [nums[i],nums[j],nums[k]]
                if sum(l) == target:
                    return sum(l)
                if abs(sum(l) - target) < distance:
                    result = sum(l)
                    distance = abs(sum(l) - target)
                elif abs(sum(l) - target) > distance:
                    k -= 1
                else:
                    j += 1
            return result

if __name__ == "__main__":
    Solution().threeSumClosest([1,1,1,1],-100)

