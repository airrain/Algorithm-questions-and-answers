"""Kruskal算法： 加边法 （实现：并查集+堆结构）
初始最小生成树边数为0，每迭代一次就选择一条满足不成环的最小代价边，
加入到最小生成树的边集合里，知道选取n-1条边。
"""
def kruskalMSI(graph):
	union_find = UnionFindSet()
	union_find.preprocessing(graph.nodes.values())

	min_heap = MinHeap()
	for edge in graph.edges:
		min_heap.push(edge)

	result = set()





class MinHeap(object):
	def __init__(self):
		self.heap,self.size = [],0

	def push(self,edge):
		self.heap.append(edge)
		if self.size != 0:
			self.insertHeap()
		self.size += 1

	def pop(self):

	def peak(self):
		return self.heap[0] 

	def getSize(self):
		return self.size

	def heapify(self):
		arr = self.heap
		index = 0
		length = self.size

		left = index * 2 + 1
		while left < length:
			



	def insertHeap(self):
		index = self.size
		parent = (index - 1) >> 1
		while parent >= 1 and self.heap[parent].weight > self.heap[index].weight:
			self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
			index = parent
			parent = (index - 1) >> 1

class UnionFindSet(object):
	def __init__(self):
		
	def processing(self,edges):

	def findFather(self,edge):

	def union(self,a,b):

	def isSameSet(self,a,b):



