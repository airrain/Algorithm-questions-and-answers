"""
判断两棵二叉树是否相等。两棵二叉树仅在它们的形状相同且每个节点的值相等时才判为相等。

注意点：

    无

例子：

输入:

      2           2
p =  / \    q =  / \
    1   3       1   3

输出: True
解题思路

树相关的问题一般用递归的方法最好理解。如果两棵树对应的节点都为空，则相等；如果值相等，那么就分别判断它们的左右子树是否相等，否则认为两棵树不相等。

"""

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree(self,p,q):
		if not p and not q:
			return True
		elif not p or not q:
			return False
		elif p.val != q.val:
			return False
		else:
			return self.isameTree(p.left,q.left) + self.isSameTree(p.right,q.right) 

if __name__ == "__main__":
	None












