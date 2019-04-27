"""
对表达式的后缀形式（也称为逆波兰表达式）进行计算并返回结果。操作符只有加减乘除四种，操作数为一个整数或者一个表达式。

注意点：

    无

例子:

输入: tokens = [“2”, “1”, “+”, “3”, “*”]

输出: 9
解题思路

后缀表达式的形式为操作数1，操作数2，操作符，也就是操作符要进行计算操作的两个数（或者表达式）在它的前方，所以在遍历列表的时候，我们要将前面的操作符压入栈中，当遇到操作符的时候，我们将它对应的操作数弹出并进行计算，计算结果可能是其他操作符的操作数，它原来是一个表达式，我们将该表达式的值计算出来了，所以应该把那个值继续压栈，遍历完整个列表的时候，计算结
束。这里特别要注意的是除法操作，因为给的表达式都是合法的，所以不用考虑除数为零的情况，但这里的除法操作是针对整数的，会对结果进行去尾操作。对负数与整数的除法操作也与Python自带的计算方式不同，Python计算-1//2结果为-1，而在这里应该为0，所以要进行特殊的处理。
"""
class Solution(object):
    def evalRPN(self,tokens):
        stack = []
        for token in tokens:
            if token not in ("+","-","*","/"):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()











