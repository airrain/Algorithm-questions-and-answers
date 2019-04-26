"""给一个int型数组，要求找出其中两个和为特定值的数的坐标。

注意点：

    返回的坐标一要比坐标二小
    最小的坐标是1，不是0

例子：

输入: numbers={2, 7, 11, 15}, target=9 输出: index1=1, index2=2
"""
class solution(object):
	def twoSum(self,sums,target):
		hash_map = {}
		for index,value in enumerate(sums):
			hash_map[value] = index
		for index1,value in enumerate(sums):
			if target - value in hash_map:
				index2 = hash_map[target - value] - index1
				if index2 != index1:
					return [index1 + 1,index2 + 1]