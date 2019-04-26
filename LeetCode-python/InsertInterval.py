"""
给出多个不重合的数据区段，现在插入一个数据区段，有重合的区段要进行合并。

注意点：

    所给的区段已经按照起始位置进行排序

例子：

输入: intervals = [2,6],[8,10],[15,18]， newInterval = [13,16]

输出: [2,6],[8,10],[13,18]
解题思路

最简单的方式就是复用 Merge Intervals 的方法，只需先将新的数据区段加入集合即可，但这样效率不高。既然原来的数据段是有序且不重合的，那么我们只需要找到哪些数据段与新的数据段重合，把这些数据段合并，并加上它左右的数据段即可。
"""
class Interval(object):
    def __init__(self,s = 0,e = 0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"

class Solution(object):
    def insert(self,intervals,newInterval):
        start,end = newInterval.start,newInterval.end
        left = list(filter(lambda x: x.end < start,intervals))


if __name__ == "__main__":
    Solution().insert()

