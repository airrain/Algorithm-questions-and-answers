"""
化简Unix系统下一个文件的绝对路径。

注意点：

    根目录的上层目录还是根目录
    可能有多个分隔符同时使用

例子：

输入: path = "/a/./b/../../c/"

输出: "/c"
解题思路

用栈来处理，碰到有效字符就压栈，遇到上层目录字符".."且栈不空时就弹出。为了最后连接字符串时头上有根目录，在栈底加一个空字符。
"""
class Solution(object):
    def simplifyPath(self,path):
        parts = path.split("/")
        result = ['']
        for part in parts:
            if part:
                if part not in ('.','..'):

if __name__ == "__main__":
    Solution().simplifyPath()


















