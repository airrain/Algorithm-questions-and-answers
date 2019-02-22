"""
给定一组长短不一的隔板，挑其中的两块板，使得板子之间能装最多的水。

注意点：

    两块板之间能装多少水是由短的那块板决定的
    选定两块板之后，它们之间的板就不存在了

例子：

输入: height=[1,1,1]
输出: 2
解题思路

我们把两块板分为左板、右板，现在考虑如下情况。假设左板高度为h，且比右板低，两块板之间的距离为w，则此时最多能装水w*h，此时我们尝试移动隔板。如果将左板向右移，那么有可能使容积变大，例如，左板右边的板子高h1（还是比右板低），此时最多装水(w-1)*h1，有可能比w*h大；如果将右板向左移，由于水的高度不能高于左板，所以容积最多为(w-1)*h，肯定比w*h小。基于上面的假设，我们只要把两块隔板依次向中间靠拢，就可以求出最大的容积。

"""
class Solution(object):
    def maxArea(self,height):
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            if height[left] < height[right]:
                area = (right - left)*height[left]
                result = max(result,area)
                left += 1
            else:
                area = (right - left)*height[right]
                result = max(result,area)
                right -= 1
        return result

if __name__ == "__main__":
    print(Solution().maxArea([2,1,1,4,3,3]))
