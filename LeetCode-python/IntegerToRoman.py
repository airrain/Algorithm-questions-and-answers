"""将一个int型的数字转化为罗马数字，范围在1-3999。下面是罗马数字的介绍及基本规则：

罗马数字采用七个罗马字母作数字、即Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）。记数的方法：

    相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3
    小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12
    小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9

注意点：

    基本数字 Ⅰ、X 、C 中的任何一个、自身连用构成数目、或者放在大数的右边连用构成数目、都不能超过三个，放在大数的左边只能用一个
    不能把基本数字 V 、L 、D中的任何一个作为小数放在大数的左边采用相减的方法构成数目，放在大数的右边采用相加的方式构成数目时只能使用一个
    V 和 X 左边的小数字只能用 Ⅰ
    L 和 C 左边的小数字只能用 X
    D 和 M 左边的小数字只能用 C

例子：

输入: num=99 输出: XCIX
"""
class Solution(object):
    def intToRoman(self,num):
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        strings = ["M","CM","D","C","XC","L","XL","IX","V","IV","I"]
        result = ''
        for i in range(len(nums)):
            while num >= nums[i]:
                num -= nums[i]
                result += strings[i]
            return result

if __name__ =='__main__':
   Solution().intToRoman(12)

