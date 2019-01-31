"""
实现一个栈，这个栈除了普通的压栈、弹出、获取栈顶元素外，还要能够在获得栈中的最小元素，且这些操作的时间复杂度为O(1)。

注意点：

    这里的弹出操作只需要去除栈顶元素，没有返回值

例子:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

解题思路

因为仍要有普通栈的功能，所以我们可以在内部用一个列表来实现普通的栈，但又需要在常量时间内返回栈内的最小元素，所以要用另外的数据结构来存当前的最小元素。栈中的最小元素会在压栈和弹出两个操作中发生改变，如果仅用一个变量来表示当前栈中的最小元素，压栈时更新该变量没有问题，但弹出时，如果弹出的就是最小的元素，那剩下栈中最小的元素需要O(n)的时间重新找出，不符合题目要求。我们可以通过另外一个栈来存储当前栈中的最小元素。在压栈时，如果最小栈的栈顶元素大于等于压入的元素，那么要对最小栈也进行压栈操作。而在弹出时，如果栈中弹出的元素与最小栈栈顶的元素相等，那我们也要对最小栈进行弹出，最小栈在弹出后，栈顶元素仍然是当前栈中最小的元素。
"""
class MainStack(object):
	def __init__(self,):
		self.stack = []
		self.minStack = []
		

	def pop(self):

	def push(self):

	def getMin(self):

	def top(self):



















