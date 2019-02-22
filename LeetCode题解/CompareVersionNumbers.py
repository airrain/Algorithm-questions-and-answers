"""
比较两个版本号v1和v2，如果v1 > v2，返回1，如果v1 < v2，返回-1，否则返回0。版本号是一个非空且仅包含数字和小数点的字符串。其中的小数点不再是它本来的意思，只是用来分隔数字。如”2.5”表示第二章的第五节。

注意点：

    无

例子:

输入: version1 = “0.1”, version2 = “1.1”

输出: -1
解题思路

根据小数点将版本号分割为一组数字字符串的列表，将两个列表从左到右依次进行比较，直到比较出结果。如果两个列表的长度不相等，把短列表后面的数字默认为是0。由于题目保证了小数点分隔的都是数字，所以可以将这些数字字符串转化为int型数据直接进行比较。
"""
class Solution(object):
    def compareVersion(self,version1,version2):
        version1_list = version1.split(".")
        version2_list = version2.split(".")
        len1 = len(version1)
        len2 = len(version2)
        for i in range(max(len1,len2)):
            v1 = int(version1_list[i]) if i < len1 else 0
            v2 = int(version2_list[i]) if i < len2 else 0
            if  v1 != v2:
                return 1 if v1 > v2 else -1
            return 0

if __name__ == "__main__":
    print(Solution().compareVersion("2.3","2.5"))














