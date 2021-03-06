"""
在一个集合（没有重复数字）中找到和为特定值的所有组合。

注意点：

    所有数字都是正数
    组合中的数字要按照从小到大的顺序
    原集合中的数字可以出现重复多次
    结果集中不能够有重复的组合
    虽然是集合，但传入的参数类型是列表

例子：

输入: candidates = [2, 3, 6, 7], target = 7 输出: [[2, 2, 3], [7]]
解题思路

采用回溯法。由于组合中的数字要按序排列，我们先将集合中的数排序。依次把数字放入组合中，因为所有数都是正数，如果当前和已经超出目标值，则放弃；如果和为目标值，则加入结果集；如果和小于目标值，则继续增加元素。由于结果集中不允许出现重复的组合，所以增加元素时只增加当前元素及之后的元素。
"""
class Solution(object):
    def combinationSum(self,candidates,target):
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combination(candidates,target,[],result)
        return result
def combination(self,candidates,target,current,result):







