"""罗列出n组括号的所有合法的排列组合。

注意点：

    只有一种括号形式"()"

例子：

输入: n = 3 输出: ['((()))', '(()())', '(())()', '()(())', '()()()']
解题思路

我们先来讨论一下什么样的排列是不合法的，由于只有一种类型的括号，所以我们只要时刻保持字符串中的左括号不少于右括号即可。例如：字符串")*"上来就右括号数目比左括号多，它就是不合法的，没有左括号来与第一个右括号组合。在进行递归的时候注意优先添加左括号，在现有右括号少于左括号的情况下，可以添加右括号。递归的结束条件是所有的括号都已加入字符串中。
"""
class Solution(object):
    def generateParentheses(self,n):
        result = []
        self.generate(n,n,"",result)
        return result

    def generate(self,left,right,str,result):
        if left == 0 and right == 0:
            result.append(str)
            return
        if left > 0:
            self.generate(left - 1,right,str + "(",result)
        if right > left:
            self.generate(left,right - 1,str + ")",result)

if __name__ == "__main__":
    print(Solution().generateParentheses(3))
