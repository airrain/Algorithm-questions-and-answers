"""
定义这样的一个链表，链表的每个节点都存有一个0-9的数字，把链表当成数字，表头为高位，表尾为地位。如1->2->3表示321，现在要对两个这样的链表求和。

注意点：

    数字的高低位，应该从从地位向高位进位
    有多种情况要考虑，如链表长度是否相等、是否进位等

例子：

输入: (2 -> 4 -> 3) + (5 -> 6 -> 4) 输出: 7 -> 0 -> 8
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
    def addTwoNumbers(self,l1,l2):
        result = ListNode(0)
        cur = result
        while l1 or l2:
            cur.val += self.addTwoNodes(l1,l2)
            if cur.val >= 10:
                cur.val -= 10
                cur.next = ListNode(1)
            else:
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
                cur = cur.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
                return result

    def addTwoNodes(self,n1,n2):
        if not n1 and n2:
             None
        if not n1:
            return n2.val
        if not n2:
            return n1.val
        return n1.val + n2.val
if __name__ =="__main__":
    list = ListNode(9)
    list.next = ListNode(8)
    print(Solution().addTwoNumbers(list, ListNode(1)).myPrint())
