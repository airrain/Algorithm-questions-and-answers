"""
将k个有序的链表拼接成一个有序的链表。

注意点：

    Python中有自带的堆排序实现heapq

例子：

输入: lists = [[1->2>10],[3->9],[5->6]] 输出: 1->2->3->5->6->9->10
解题思路

整体思路与Merge Two Lists相同。不过就是从原来的两个数中取最小的节点改为从k个数中取最小的节点。这是一个典型的堆排序的应用，Python中堆排序可以用heapq实现。
"""
import heapq
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self,lists):




