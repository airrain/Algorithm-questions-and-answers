"""
数组中的每个值表示在当前位置最多能向前面跳几步，判断给出的数组是否否存在一种跳法跳到最后。

注意点：

    所有的数字都是正数
    跳的步数可以比当前的值小

例子：

输入: nums = [2, 3, 1, 1, 4]

输出: True

输入: nums = [3, 2, 1, 0, 4]

输出: False
解题思路

先想一下什么时候不能够完成跳跃，在当前位置之前（包括当前位置）能够跳跃到的最远距离就是当前位置，且这时候还没有到终点；什么样的情况就能保证可以跳到终点呢，只要当前最远距离超过终点即可。只要当前的位置没有超过能跳到的最远距离，就可以不断的刷新最远距离来继续前进。
"""
class Solution(object):
    def canJump(self,nums):
        if not nums:
            return False
        length = len(nums)
        index = 0
        longest = nums[0]
        while index <= longest:
            if longest >= length - 1:
                return True
            longest = max(longest,index + nums[longest])
            index += 1
        return False

if  __name__ == "__main__":
    Solution().canJump([2,3,1,5,2])

