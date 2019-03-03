"""
找出两个单向链表是在哪个节点开始合二为一的。

注意点：

    如果没有交集，那么返回None
    返回结果时要保证链表还是原来的结构
    链表中没有环形结构
    最好时间复杂度为O(n)，空间复杂度为O(1)

例子:

输入：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

输出： c1
解题思路

最容易想到的方法是双指针，在交点之前，两个链表的长度不同，如果我们知道他们的长度差，那么只要在长的链表上先前进他们相差的节点数，然后两个指针同时各自在两个链表上前进，那么当他们相遇的时候就是第一个相交的节点。而那个差就是两个链表的长度差，因为它们的后半部分是相同的。

上面是通过让长链表上的指针先走的方法，其实我们也可以在链表前加长，使得它们在交点之前的长度相等，在上面的例子中，我们可以在链表A之前加上一个链表B，在链表B之前加上一个链表A，这时两条链表的总长度相同，都是原来两条链表的长度和，那么在它们交点前的链表长度也是相等的。让两个指针同时前进直到相交即可。

还可以通过复用Linked List Cycle II的代码来实现，我们将链表A的尾部连接到它的头部，这道题就变成找出链表中环的起始位置了。不过要记得将链表恢复原样。
"""
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        nodeA,nodeB = neadA,headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA

    def getIntersectionNode_diff(self,headA,headB):
        def get_length(node):
