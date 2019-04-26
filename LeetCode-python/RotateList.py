"""
将一个链表中的元素向右旋转k个位置。

注意点：

    k可能非常大
    最好不要申请额外空间

例子：

输入: list = 1->2->3->4->5->NULL, k = 2

输出: 4->5->1->2->3->NULL
解题思路

如果能有链表的长度，就不用担心k非常大而不断的循环旋转了。所谓的旋转其实就是在链表中间断开，首尾相连。在获取链表长度的时候顺便把链表的首尾连起来。注意断开的位置是在倒数第k个之前。
"""
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()

    class Solution(object):
        def rotateRight(self,head,k):




if __name__  == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    result = Solution().rotateRight(l1,2)
    result.myPrint()


