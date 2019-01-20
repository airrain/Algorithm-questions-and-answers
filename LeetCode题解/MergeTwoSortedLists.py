"""
将两个有序的链表拼接成一个有序的链表。

注意点：

    不需要额外申请节点，主要把原链表中的节点串联起来
    原链表中的一个已经全部在新链表中后，另一个链表剩余的部分可以直接拼接

例子：

输入: l1 = 1->2->4, l2 = 3 输出: 1->2->3->4
解题思路

为了避免分类讨论，添加一个假的头节点。现在只需要两个指针分别指向原来的两个链表，将其中比较小的节点添加到新的链表中。传入的参数l1和l2正好可以当作遍历两个链表的指针。
"""
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoSortedLists(self,l1,l2):
		temp = ListNode(-1)
		head = temp
		while l1 and l2:
			if l1.val > l2.val:
				temp.next = l1.val
				l1 = l1.next
			else:
				temp.next = l2.val
				l2 = l2.next
			temp = temp.next
		if l1:
			temp.next = l1
		else:
			temp.next = l2
		return head.next

if __name__ == '__main__':
	Solution().mergeTwoSortedLists(ListNode(1),ListNode(2))

