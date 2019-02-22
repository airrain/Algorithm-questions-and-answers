"""
将所含字母相同，但排列顺序不同的字符串归并到一起。

注意点：

    所有输入的字符都是小写的
    返回结果中每个组的字符串都要按照字典序排列

例子：

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [ ["ate", "eat","tea"], ["nat","tan"], ["bat"] ]
解题思路

将每个字符串排序，并把排序后相同的字符串归为一组，将每组字符串排序后即为所要的结果。
"""
class Solution(object):
    def groupAnagrams(self,strs):
        map = {}
        for i,v in enumerate(strs):
            target = "".join(sorted(v))
            if target not in map:
                map[target] = [v]
            else:
                map[target].append(v)

        result = []
        for value in map.value():
            result += [sorted(value)]
        return result

if __name__ == "__main__":
    Solution().groupAnagrams(["eat","bar","bat","ate"])






















