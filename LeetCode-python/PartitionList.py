"""
给定一个链表以及一个目标值，把小于该目标值的所有节点都移至链表的前端，大于等于目标值的节点移至链表的尾端，同时要保持这两部分在原先链表中的相对位置。

注意点：

    链表的排序一般通过重新连接指针来完成

例子：

输入: head = 1->4->3->2->5->2, x = 3

输出: 1->2->2->4->3->5
解题思路

看成有一串珠子，有红和蓝两种颜色，现在要把红色和蓝色分别集中到一起。可以遍历每个珠子，如果是蓝色就串在一条线上，红色的串在另一条线上，最后把两条线连起来就可以了。注意，在比较大的那串数中，最后的指针要置为None，因为那是排序后的最后一个节点。
"""
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution(object):
    def partition(self,head,x):
        dummy = ListNode(-1)
        dummy.next = head
        small_dummy = ListNode(-1)
        large_dummy = ListNode(-1)

        prex = dummy
        small_prev = small_dummy
        large_prev = large_dummy
        while prev.next:
            curr = prev.next
            if curr.val < x:
                small_prve.next = curr
                small_prev  = small_prev.next
            else:
                large_prev.next = curr
                large_prev = large_prev.next
            prev = prev.next
        large_prev.next = None
        small_prev.next = large_dummy.next
        return small_dummy.next

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    r = Solution().partition(n1,3)
    r.to_list()

