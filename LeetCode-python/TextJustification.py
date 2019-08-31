'''把一个集合的单词按照每行L个字符存放，不足的在单词间添加空格，
每行要两端对齐(即两端都要是单词)，如果空格不能均匀分布在所有间隔中，
那么左边的空格要多于右边的空格，最后一行靠左对齐，每个单词间一个空格。

注意点：

    单词的顺序不能发生改变
    中间行也可能出现只有一个单词，这时要靠左对齐
    每行要尽可能多的容纳单词
'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        start = end = 0
        result, curr_words_length = [], 0
        for i, word in enumerate(words):
            if len(word) + curr_words_length + end - start  > maxWidth:
                if end - start == 1:
                    result.append(words[start] + ' ' * (maxWidth - curr_words_length))
                else:
                    total_space = maxWidth - curr_words_length
                    space, extra = divmod(total_space, end - start - 1)
                    for j in range(extra):
                        words[start + j] += ' '
                    result.append((' ' * space).join(words[start:end]))
                curr_words_length = 0
                start = end = i
            end += 1
            curr_words_length += len(word)
        result.append(' '.join(words[start:end]) + ' ' * (maxWidth - curr_words_length - (end - start - 1)))
        return result


if __name__ == "__main__":
    Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]