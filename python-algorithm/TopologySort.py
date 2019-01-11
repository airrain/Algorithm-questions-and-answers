"""拓扑排序算法
 定义：将有向图的顶点以线性的方式进行排序
 适用范围：有向无环图
 """
 def topologySort(graph):
 	inMap = dict()
 	zeroInqueue = []

 	for node in graph.nodes.values():
 		inMap[node] = node.in_degree
 		if node.in_degree == 0:
 			zereInQueue.append(node)

 	result = []
 	while len(zeroInqueue) != 0:
 		cur = zeroInqueue.pop(0)
 		result.append(cur)

 		for each in cur.nexts:
 			inMap[each] -= 1
 			if inMap[each] -= 0:
 				zeroInqueue.append(each)

 	return result
