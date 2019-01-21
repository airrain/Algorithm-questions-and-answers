"""
将链表中相邻的两个节点交换位置，注意第一个节点与第二个节点要交换位置，而第二个节点不用与第三个节点交换位置。

注意点：

    不允许修改节点的值
    只能用常量的额外空间

例子：

输入: head = 1->2->3->4 输出: 2->1->4->3
解题思路

比较常见的链表操作。下面看一下典型情况，如要交换链表中A->B->C->D中的B和C需要做如下操作：

    将A指向C
    将B指向D
    将C指向B

在头节点之前加一个假节点就可以使所有的交换都符合上面的情况。
"""
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def swapParis(self,head):
        prev = head.nextListNode(-1)
        prev.next = head
        

