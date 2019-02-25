"""
实现树的广度优先遍历，每一层上的数据按照从左到右的顺序排列。

注意点：

    无

例子：

输入:

    3
   / \
  9  20
    /  \
   15   7

输出:

[
  [3],
  [9,20],
  [15,7]
]

解题思路

将树每一层的节点存在一个列表中，遍历列表中的元素，如果该节点有左右节点的话，就把它们加入一个临时列表，这样当遍历结束时，下一层的节点也按照顺序存储好了，不断循环直到下一层的列表为空。

"""
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self,root):
        result = []
        if not root:
            return result
        curr_level = [root]
        while curr_level:
            level_result = []
            next_level = []











