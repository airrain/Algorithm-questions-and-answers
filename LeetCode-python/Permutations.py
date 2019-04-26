"""
输出一个没有重复数字的数组的全排列。

注意点：

    不用考虑重复数字的情况

例子：

输入: nums = [1, 2, 3] 输出: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
解题思路

这道题比较单间，采用递归把数组中的数字依次加入当前数组current来进行排列组合。
"""
class Solution(object):
    def permute(self,nums):
        result = []
        self.get_permute([],nums,result)
        return result

    def get_permute(self,current,num,result):
        if not num:
            result.append(current + [])
            return
        for i, v in enumerate(num):
            current.append(num[i])
            self.get_permute(current,num[:i] + num[i + 1:],result)
            current.pop()

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))