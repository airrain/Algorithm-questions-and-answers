"""
编写一个算法来确定一个数字是否“快乐”。 快乐的数字按照如下方式确定：从一个正整数开始，用其每位数的平方之和取代该数，并重复这个过程，直到最后数字要么收敛等于1且一直等于1，要么将无休止地循环下去且最终不会收敛等于1。能够最终收敛等于1的数就是快乐的数字。

例如：19是一个快乐数字，计算过程如下：

    1^2+9^2=82
    8^2+2^2=68
    6^2+8^2=100
    1^2+0^2+0^2=1

要求：当输入快乐的数字时，输出True，否则输出False。

思路：
1. 当输入的不是快乐数字时，会陷入一个无限循环，因此增加一个计数器 count 用来统计计算次数。设定当 count 达到2000次时，认为该数字不是快乐数字，跳出循环结束计算。（这里我认为直接设定一个最大循环次数不怎么科学，但是暂时没有想到更有说服力的方法来决定何时结束循环。）注：已有一方法解决该问题，见最下方更新部分。
2. 因为不确定输入的数字会是几位数，因此不采用除法和取模的方法来获得数字的每一位数，而是利用 for 循环获取字符串类型数字的每一位来计算平方和。

"""
class Solution(object):
    def getSumOfSquares(self,num):
        numStr = str(num)
        sum = 0
        digitls = [int(x) for x in numStr]
        for i in digitls:
            sum += i * 2
        return sum

if __name__  == "__main__":
        n = input()
        sumOfSqrs = eval(n)
        count = 0
        while sumOfSqrs != 1:
            sumOfSqrs = Solution().getSumOfSquares(sumOfSqrs)
            count += 1
            if count > 5:
                print("False")
        else:
            print("True")






