"""
有一群人站队，每人通过一对整数(h, k)来描述，其中h表示人的高度，k表示在此人前面队列中身高不小于此人的总人数。
实现一个算法输出这个队列的正确顺序。

输入格式：
输入格式为二维列表，即 list[list[]]形式
外层list包含队列中全部的人，内层list为[h,k]格式，代表个人信息。

输出格式：
输出格式为：list[list[int]]形式
与输入格式一样，需要按照队列顺序排列。

示例：
输入：[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出：[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
inputls = eval(input())
inputls = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
sortls = sorted(inputls)
num = len(sortls)
indexls = list(range(num))
output = list(range(num))
pops = []
for x in range(num):









