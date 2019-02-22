"""
找出一个由纯数字组成的序列能够构成的不同的IP地址。

注意点：

    每个IP段的范围是0-255
    要用整个序列，而不是它的子集

例子：

输入: s = "25525511135"

输出: ["255.255.11.135", "255.255.111.35"]
解题思路

每次把1到3个数字当作一个IP段，多个数字时要注意首位不能为0，因为 01.0.0.0 这样的IP是不符合规范的，此外三个数字时还不能超过255。当递归的序列为空，且此时正好集齐四个IP段，则得到一个正确答案。在递归的序列为空或者IP段数目达到4时都应该终止递归。
"""
class Solution(object):
    def restoreIpAddresses(self,s):
        result = []
        self._restoreIpAddresses(0,s,[],result)
        return result
    def _restoreIpAddresses(self,):









