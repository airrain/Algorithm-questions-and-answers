"""
给定一个起始字符串和一个目标字符串，现在将起始字符串按照特定的变换规则转换为目标字符串，求最少要进行多少次转换。转换规则为每次只能改变字符串中的一个字符，且每次转换后的字符串都要在给定的字符串集合中。

注意点：

    如果无法完成转换则返回0
    所有给出的字符串的长度都相等
    所有的字符都为小写字母

例子:

输入: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]

输出: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
解题思路

因为每次变换后的字符串都要在给定的字符串组中，所以每次变化的情况都是有限的。现在把变化过程做成一个树的结构，由某一个字符串变化而来的字符串就成为该字符串的子树。参看下图的例子，我们可以得到以下几点结论：

    我们把起始字符串当成根节点，如果在变化过程中，某一个节点是目标字符串，那么就找到了一条变化路径。
    节点所在的高度能够反映出变化到该节点时经历了几次变化，如hot在根节点的下一层，表示变化了一次，hut和bot在更下一层，表示变化了两次。
    在树上层出现过的字符串没必要在下层再次出现，因为如果该字符串是转换过程中必须经过的中间字符串，那么应该挑选上层的该字符串继续进行变化，它的转换次数少。
    如果上一层有多个字符串可以转换为下一层同一个字符串，那么只需要找到其中一个转换关系即可，如例子中的bit和him都可以转为bim，我们只需要知道有一条关系可以走到bim就可以了，没必要找到所有的转换关系，因为这样已经可以确定进行两次转换就能变为bim。
    基于第3和第4点，当集合中的字符串在树中出现后，就可以把它从集合中删除。这样可以防止字符串不断地循环转化。
    至此，这个问题就变为一个深度优先遍历问题，只需要依次遍历每一层的节点，如果在该层找到了目标字符串，只要返回相应的变化次数。如果到某一层树的节点无法继续向下延伸，且没有找到目标字符串，那么就是不存在这样的转换关系，返回0。 word ladder

        注：图中的有些单词没有意义，只是单纯为了举例子，图对应的起始字符串为hit，给定的字符串集合为{"hot","hat","bit","him","bot","bim"}
"""
class Solution(object):
	def ladderLength(self,beginWord,endWord,wordList):
		